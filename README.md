# dopa code reverse shell

<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-111111?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/security-research-8b0000?style=for-the-badge">
  <img src="https://img.shields.io/badge/status-experimental-222222?style=for-the-badge">
  <img src="https://img.shields.io/badge/license-mit-111111?style=for-the-badge">
</p>

<p align="center">

```text
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀
⠀⠀⣰⠋⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⠳⡄⠀⠀
⢀⡾⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠙⣆⠀
⢸⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠘⡄
⢸⠀⢠⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⢀⠄⢰⠁
⢸⠀⠈⣆⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⡜⠀⢸⠀
⠸⡄⠀⠸⡄⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⡸⠁⠀⣸⠀
⠀⢻⡄⠀⢱⡀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⢠⠃⠀⣰⠇⠀
⠀⠀⢻⡄⠀⢧⠀⡀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⢠⢀⠏⠀⣴⠏⠀⠀
⠀⠀⠀⢻⣆⠘⣆⢣⠀⠀⠳⣄⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⠟⢛⡛⠛⠛⠛⢛⣛⡛⠛⠛⠛⢻⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⡴⠋⠀⢠⠇⡼⠀⣼⠋⠀⠀⠀
⠀⠀⠀⠀⢹⣦⢹⡄⣇⠀⡀⠈⠳⣤⣶⣿⣿⣿⣿⡿⠻⣧⡙⢷⡌⠀⠀⠀⠀⠀⠀⠀⠀⠈⣰⡟⣡⡿⠛⢿⣿⣿⣿⣿⣦⣤⠞⠁⢀⠀⡎⣰⢃⣾⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣷⣷⠸⡄⢱⡀⠀⠀⠉⢹⣿⣿⠃⠖⠀⠈⣿⡜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⠏⠀⠀⠀⠹⣿⣿⠋⠁⠀⠀⢠⠃⣸⢱⣧⣾⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣧⢳⡀⢳⡀⠀⠀⢸⣿⠃⡂⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⣀⡀⠹⣿⠀⠀⠀⢠⠃⢠⢇⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣿⣾⣇⠀⢷⡀⠀⣾⢃⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣆⢻⣇⠀⣠⡏⢀⣾⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡆⠈⢷⣼⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣴⡟⠀⣼⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⡿⠛⢿⣿⣿⡀⣼⠏⣿⠃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣯⢻⣄⢰⣿⣿⡿⢻⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⢿⡄⠀⢻⣿⡟⢡⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠙⣻⣿⠏⠀⣰⣟⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣼⣷⡀⠀⢿⣷⠘⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠰⢠⣿⡇⠂⣰⣿⣼⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣻⣿⡇⢰⣿⡏⠠⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⢠⠘⢿⣧⡀⢿⣿⣻⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠟⠀⣿⣿⠀⣠⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣤⣀⢸⣿⡇⠚⢿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠘⠢⠘⣿⣿⡟⠡⠄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡇⠀⠐⠀⠀⠀⢿⣄⠁⠀⠀⠀⠀⠀⠀⠀⠂⠀⠙⣿⣿⡿⢁⠀⣸⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⣦⡀⠈⢿⣿⣦⣀⠁⠀⠀⣀⣀⣀⣠⣴⣿⣟⠀⠀⠀⠀⠀⠀⠈⣿⣷⣤⣀⣀⣀⣀⠀⠀⢀⣠⣾⣿⣟⢡⣿⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⡇⠹⣷⡔⠸⣧⠉⠛⠛⠛⠛⠉⠉⠉⠙⠻⣿⣿⡆⡄⠀⠀⠀⠀⣾⣿⡿⠛⠉⠉⠉⠉⠛⠛⠛⠋⢁⡿⠘⣼⡿⢁⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⢰⣿⣇⢠⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡇⠀⠀⠀⠀⠀⣿⡿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣡⢦⣿⣧⡜⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⡇⢸⣿⣿⠘⠃⠈⠙⠿⠶⣶⣤⣤⣴⣶⣿⣥⣿⠇⠀⠀⠀⠀⠀⢿⣧⣬⣷⣶⣤⣤⣴⡶⠶⠟⠉⠀⠀⢸⣿⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣷⣼⣿⢿⣧⡀⠀⡀⠀⡀⠀⣀⣤⣀⡀⣌⠻⣷⡐⠀⠀⠀⠀⠀⣠⡟⠉⠀⢀⣀⣄⡀⠀⠀⠀⠀⠀⣠⣾⡿⣿⣤⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡇⡌⠻⣿⣦⣈⣉⣴⣾⣿⣯⣿⣿⠈⠂⠈⠁⠀⠀⠀⠀⠀⠉⠀⠀⢰⢿⣿⣿⣿⣦⣄⣀⣠⣾⣿⠏⠀⣿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠁⠀⠈⠛⢿⣿⣟⠁⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣈⣿⡇⠛⣿⣿⠟⠋⠵⠂⠀⠸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡄⠇⢰⣆⠀⠈⣷⢹⣦⠙⢿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠿⢃⣾⢻⡟⠈⢀⣾⠃⠀⣼⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣄⠀⠹⣆⠀⢸⣿⣿⣧⠀⢀⣿⠻⣿⣷⣌⠀⠀⠀⠀⢀⣤⣿⡿⢻⣿⠀⢠⣿⣿⣿⢁⢀⣾⢃⣠⣾⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⡀⢿⣧⠀⢿⣿⣿⡆⣾⢻⡆⣈⠻⣿⣷⣦⣤⣴⣿⡿⠋⡄⣼⢻⣄⣾⣿⣿⡏⢠⣿⠃⣰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣆⣿⣧⠸⣿⣿⣿⣿⠈⣷⡙⠳⠆⠉⠉⠉⠉⠁⠀⠁⣠⡟⠀⣿⣿⣿⡿⢠⣿⢁⣼⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣿⣿⣿⣿⠀⢹⣿⡟⢶⡦⣤⣤⣤⣶⠾⣿⣻⠃⢀⣿⣿⣿⢧⣿⣷⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⠟⣋⣸⡀⠀⢳⡉⠙⠓⠛⠓⠛⠚⠉⣩⠏⠀⢸⣄⡙⢿⣾⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡿⣿⣿⣧⠀⠀⢹⣀⣀⣀⣀⣀⣀⣰⠃⠀⢠⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣧⢻⣿⠿⣷⣄⣼⣇⣠⣧⣇⣿⣀⣸⣄⣠⣿⢟⣿⢃⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡄⠻⣷⣤⣬⣥⠿⠿⠿⠿⠿⠿⢯⣭⣤⣴⡿⠃⣸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⡀⠤⡍⠁⠀⠀⠀⠀⠒⠀⠀⡀⡄⠉⣉⠀⣰⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⣤⣤⣤⣤⣴⣶⣷⣶⣤⣤⣤⣤⣴⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠋⠉⠁⠀⠀⠀⠉⠉⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```

### `dopa code / reverse shell`

**controlled remote shell for authorized security research**

</p>

---

## ⚠ authorization required

> **this project is intended exclusively for systems owned by you or systems for which you have explicit authorization to perform security testing.**

This software provides remote command-execution and system-interaction capabilities that can be dangerous outside an isolated laboratory.

Unauthorized access, data collection, persistence, or execution on another person's computer may violate criminal and computer-access laws.

**use it only inside controlled environments such as:**

* 🧪 personal laboratory machines
* 🖥️ isolated virtual machines
* 🎯 authorized penetration-testing engagements
* 🏴‍☠️ ctf environments
* 🔬 malware-analysis sandboxes
* 🛡️ defensive security research

The author assumes no responsibility for unauthorized or unlawful use.

---

## overview

`dopa code reverse shell` is a Python-based research project designed to demonstrate the architecture of a reverse shell.

Instead of waiting for an inbound connection, the client establishes an outbound TCP connection to a configured listener.

```text
┌─────────────────────┐
│     test machine    │
│                     │
│  reverseshell.py    │
└──────────┬──────────┘
           │
           │ TCP
           │ outbound
           ▼
┌─────────────────────┐
│       listener      │
│                     │
│      operator       │
└─────────────────────┘
```

The project is primarily useful for understanding:

* TCP socket communication
* remote command processing
* process execution
* file-transfer protocols
* system enumeration
* connection handling
* reconnection logic
* security-tool detection

---

## capabilities

| capability             | description                                 |
| ---------------------- | ------------------------------------------- |
| `socket communication` | TCP client/listener communication           |
| `command execution`    | Execute commands through the local shell    |
| `powershell`           | Windows PowerShell command handling         |
| `file transfer`        | Transfer files using Base64 encoding        |
| `system information`   | Collect basic host information              |
| `process management`   | Enumerate and manage processes              |
| `screenshot`           | Capture the primary display on Windows      |
| `reconnection`         | Automatically reconnect after disconnection |
| `shutdown marker`      | Local mechanism for stopping the client     |
| `hash verification`    | SHA-256 integrity information for transfers |

> Some functionality is intentionally Windows-oriented.

---

## architecture

```text
                         TCP / 4444
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                        test environment                      │
│                                                              │
│   ┌─────────────────────┐          ┌─────────────────────┐   │
│   │   reverse shell     │          │      listener       │   │
│   │                     │          │                     │   │
│   │  Python 3           │ ──────►  │  TCP socket         │   │
│   │  socket             │          │  command input      │   │
│   │  subprocess         │ ◄──────  │  output             │   │
│   │  file handling      │          │                     │   │
│   └─────────────────────┘          └─────────────────────┘   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## project structure

```text
dopa-code-reverse-shell/
│
├── reverseshell.py
├── documentation
├── requirements.txt
├── license
└── README.md
```

The main implementation is intentionally kept in a single Python file so the networking and command-dispatch architecture can be studied easily.

---

## requirements

The client uses **Python's standard library**.

No external Python packages are required.

Main modules include:

```text
socket
os
sys
subprocess
base64
time
shutil
platform
json
hashlib
```

Python:

```text
Python 3.6+
```

For a controlled local laboratory, the listener can be implemented with a standard TCP networking utility.

---

## configuration

The connection parameters are defined near the beginning of the script:

```python
HOST = "127.0.0.1"
PORT = 4444
RECONNECT_DELAY = 5
MAX_RECONNECTS = -1
STARTUP_DELAY = 0
```

For local testing:

```text
127.0.0.1:4444
```

keeps the experiment restricted to the same machine.

For an authorized multi-machine laboratory, configure the address of the designated test listener.

---

## command interface

The client exposes a command dispatcher supporting operations such as:

```text
help
pwd
cd <directory>
ls
cat <file>
mkdir <directory>
mv <source> <destination>
rm <path>

shell <command>
powershell <command>
ps <command>

pslist
kill <pid>

info
sysinfo

screenshot

download <path>
upload <path>

sleep <seconds>

cls
exit
die
```

The exact behavior depends on the operating system and the permissions available to the process.

---

## connection lifecycle

The client follows a simple lifecycle:

```text
                ┌──────────────┐
                │    START     │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ create socket │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ connect TCP  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ receive cmd  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ dispatch cmd │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ send result  │
                └──────┬───────┘
                       │
                       └──────────────┐
                                      │
                              connection lost
                                      │
                                      ▼
                               reconnect delay
                                      │
                                      └──────► connect
```

---

## file transfer

File transfers use Base64 encoding and SHA-256 hashes.

Conceptually:

```text
file
 │
 ▼
read bytes
 │
 ▼
base64 encode
 │
 ▼
split into chunks
 │
 ▼
TCP transmission
 │
 ▼
base64 decode
 │
 ▼
write file
 │
 ▼
SHA-256 verification
```

This mechanism is intended for studying basic application-layer file-transfer protocols.

---

## system information

The `info` command returns information such as:

```json
{
  "hostname": "...",
  "system": "Windows",
  "release": "...",
  "machine": "...",
  "processor": "...",
  "cwd": "...",
  "username": "...",
  "python": "..."
}
```

This is useful for demonstrating how applications can query their execution environment.

---

## security considerations

This project deliberately demonstrates capabilities that security products commonly treat as suspicious.

A reverse shell can provide extensive control over the host running it.

Potential risks include:

* arbitrary command execution
* access to local files
* process manipulation
* screen capture
* remote file transfer
* persistent execution mechanisms
* remote payload execution

**Do not execute this software on machines you do not own or have explicit authorization to test.**

---

## laboratory recommendation

For safe experimentation, use an isolated environment:

```text
┌─────────────────────────────┐
│       HOST MACHINE          │
│                             │
│  ┌───────────────────────┐  │
│  │     LAB NETWORK       │  │
│  │                       │  │
│  │  ┌───────┐  ┌───────┐ │  │
│  │  │ TEST  │  │ TEST  │ │  │
│  │  │ VM 01 │  │ VM 02 │ │  │
│  │  └───────┘  └───────┘ │  │
│  │                       │  │
│  └───────────────────────┘  │
│                             │
└─────────────────────────────┘
```

Recommended controls:

* isolated virtual network
* snapshots before testing
* no production credentials
* no personal files
* no access to third-party systems
* monitoring enabled
* clearly defined testing scope

---

## limitations

This project is intentionally simple and should **not** be considered a production remote-management system.

Known limitations include:

* TCP communication is not inherently encrypted.
* Authentication is not implemented.
* File transfers are loaded into memory.
* Some features are Windows-specific.
* The protocol is intentionally simple.
* Network interruptions can affect transfers.
* Security software may detect the behavior.

---

## project status

```text
status        experimental
language      python
platform      windows / linux
purpose       security research
environment   authorized laboratories
```

This repository exists as a technical and educational exploration of reverse-shell architecture.

---

## responsible use

By using this project, you acknowledge that you are responsible for operating it within the laws and authorization requirements applicable to your environment.

**authorized testing only.**

```text

⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀
⠀⠀⣰⠋⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⠳⡄⠀⠀
⢀⡾⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠙⣆⠀
⢸⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠘⡄
⢸⠀⢠⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⢀⠄⢰⠁
⢸⠀⠈⣆⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⡜⠀⢸⠀
⠸⡄⠀⠸⡄⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⡸⠁⠀⣸⠀
⠀⢻⡄⠀⢱⡀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⢠⠃⠀⣰⠇⠀
⠀⠀⢻⡄⠀⢧⠀⡀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⢠⢀⠏⠀⣴⠏⠀⠀
⠀⠀⠀⢻⣆⠘⣆⢣⠀⠀⠳⣄⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⠟⢛⡛⠛⠛⠛⢛⣛⡛⠛⠛⠛⢻⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⡴⠋⠀⢠⠇⡼⠀⣼⠋⠀⠀⠀
⠀⠀⠀⠀⢹⣦⢹⡄⣇⠀⡀⠈⠳⣤⣶⣿⣿⣿⣿⡿⠻⣧⡙⢷⡌⠀⠀⠀⠀⠀⠀⠀⠀⠈⣰⡟⣡⡿⠛⢿⣿⣿⣿⣿⣦⣤⠞⠁⢀⠀⡎⣰⢃⣾⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣷⣷⠸⡄⢱⡀⠀⠀⠉⢹⣿⣿⠃⠖⠀⠈⣿⡜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⠏⠀⠀⠀⠹⣿⣿⠋⠁⠀⠀⢠⠃⣸⢱⣧⣾⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣧⢳⡀⢳⡀⠀⠀⢸⣿⠃⡂⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⣀⡀⠹⣿⠀⠀⠀⢠⠃⢠⢇⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣿⣾⣇⠀⢷⡀⠀⣾⢃⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣆⢻⣇⠀⣠⡏⢀⣾⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡆⠈⢷⣼⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣴⡟⠀⣼⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⡿⠛⢿⣿⣿⡀⣼⠏⣿⠃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣯⢻⣄⢰⣿⣿⡿⢻⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⢿⡄⠀⢻⣿⡟⢡⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠙⣻⣿⠏⠀⣰⣟⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣼⣷⡀⠀⢿⣷⠘⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠰⢠⣿⡇⠂⣰⣿⣼⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣻⣿⡇⢰⣿⡏⠠⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⢠⠘⢿⣧⡀⢿⣿⣻⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠟⠀⣿⣿⠀⣠⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣤⣀⢸⣿⡇⠚⢿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠘⠢⠘⣿⣿⡟⠡⠄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡇⠀⠐⠀⠀⠀⢿⣄⠁⠀⠀⠀⠀⠀⠀⠀⠂⠀⠙⣿⣿⡿⢁⠀⣸⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⣦⡀⠈⢿⣿⣦⣀⠁⠀⠀⣀⣀⣀⣠⣴⣿⣟⠀⠀⠀⠀⠀⠀⠈⣿⣷⣤⣀⣀⣀⣀⠀⠀⢀⣠⣾⣿⣟⢡⣿⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⡇⠹⣷⡔⠸⣧⠉⠛⠛⠛⠛⠉⠉⠉⠙⠻⣿⣿⡆⡄⠀⠀⠀⠀⣾⣿⡿⠛⠉⠉⠉⠉⠛⠛⠛⠋⢁⡿⠘⣼⡿⢁⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⢰⣿⣇⢠⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡇⠀⠀⠀⠀⠀⣿⡿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣡⢦⣿⣧⡜⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⡇⢸⣿⣿⠘⠃⠈⠙⠿⠶⣶⣤⣤⣴⣶⣿⣥⣿⠇⠀⠀⠀⠀⠀⢿⣧⣬⣷⣶⣤⣤⣴⡶⠶⠟⠉⠀⠀⢸⣿⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣷⣼⣿⢿⣧⡀⠀⡀⠀⡀⠀⣀⣤⣀⡀⣌⠻⣷⡐⠀⠀⠀⠀⠀⣠⡟⠉⠀⢀⣀⣄⡀⠀⠀⠀⠀⠀⣠⣾⡿⣿⣤⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡇⡌⠻⣿⣦⣈⣉⣴⣾⣿⣯⣿⣿⠈⠂⠈⠁⠀⠀⠀⠀⠀⠉⠀⠀⢰⢿⣿⣿⣿⣦⣄⣀⣠⣾⣿⠏⠀⣿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠁⠀⠈⠛⢿⣿⣟⠁⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣈⣿⡇⠛⣿⣿⠟⠋⠵⠂⠀⠸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡄⠇⢰⣆⠀⠈⣷⢹⣦⠙⢿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠿⢃⣾⢻⡟⠈⢀⣾⠃⠀⣼⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣄⠀⠹⣆⠀⢸⣿⣿⣧⠀⢀⣿⠻⣿⣷⣌⠀⠀⠀⠀⢀⣤⣿⡿⢻⣿⠀⢠⣿⣿⣿⢁⢀⣾⢃⣠⣾⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⡀⢿⣧⠀⢿⣿⣿⡆⣾⢻⡆⣈⠻⣿⣷⣦⣤⣴⣿⡿⠋⡄⣼⢻⣄⣾⣿⣿⡏⢠⣿⠃⣰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣆⣿⣧⠸⣿⣿⣿⣿⠈⣷⡙⠳⠆⠉⠉⠉⠉⠁⠀⠁⣠⡟⠀⣿⣿⣿⡿⢠⣿⢁⣼⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣿⣿⣿⣿⠀⢹⣿⡟⢶⡦⣤⣤⣤⣶⠾⣿⣻⠃⢀⣿⣿⣿⢧⣿⣷⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⠟⣋⣸⡀⠀⢳⡉⠙⠓⠛⠓⠛⠚⠉⣩⠏⠀⢸⣄⡙⢿⣾⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡿⣿⣿⣧⠀⠀⢹⣀⣀⣀⣀⣀⣀⣰⠃⠀⢠⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣧⢻⣿⠿⣷⣄⣼⣇⣠⣧⣇⣿⣀⣸⣄⣠⣿⢟⣿⢃⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡄⠻⣷⣤⣬⣥⠿⠿⠿⠿⠿⠿⢯⣭⣤⣴⡿⠃⣸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⡀⠤⡍⠁⠀⠀⠀⠀⠒⠀⠀⡀⡄⠉⣉⠀⣰⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⣤⣤⣤⣤⣴⣶⣷⣶⣤⣤⣤⣤⣴⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠋⠉⠁⠀⠀⠀⠉⠉⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                    dopa code / reverse shell

                         ⚠ authorized testing only ⚠
```
## connect

<p align="center">
  <a href="https://instagram.com/ju4nito_zzz">
    <img src="https://img.shields.io/badge/Instagram-@dopacodee-111111?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
  </a>
</p>

<p align="center">
  <sub>© dopa code · security research</sub>
</p>
