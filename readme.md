# BetterDiscord Monitor

Monitors BetterDiscord for when a host update or stale heartbeat breaks the install, and automatically triggers the BetterDiscord installer to restore it.

---

## 📋 Features

- **Heartbeat Monitoring:** Checks a heartbeat file written by a BetterDiscord plugin to confirm it's still running.
- **Discord Update Detection:** Detects if Discord has updated and reinstalls BetterDiscord automatically.
- **System Tray Integration:** Runs silently in the tray with options to show logs or exit.
- **Notifications:** Displays a notification when reinstalling BetterDiscord.
- **Installer Helper:** Bundles the BetterDiscord installer for automatic repair.
- **Lightweight:** Very low CPU and RAM usage.

---

## ⚠️ Disclaimer

- I am **not affiliated with Discord or BetterDiscord**.
- This project is unofficial and provided **as-is**.
- If any party (Discord or BetterDiscord) requests removal, I will comply immediately.
- Use at your own risk.

---

## 🚀 Getting Started

Clone the repository:
git clone https://github.com/YourUsername/BetterDiscord-Monitor.git
cd BetterDiscord-Monitor
Install dependencies:

pip install -r requirements.txt


🖥️ Running in Development
Run the monitor in a terminal:
python main.py
Note:
By default, logs will be written to logs.txt.
You will not see console output unless you tail the log file:

Windows PowerShell:
Get-Content .\logs.txt -Wait

🛠️ Customizing Log Behavior
If you want logs printed to the console instead of logs.txt, open monitor.py and:

Remove or comment out:
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
Replace each logging.info(...) with:
print(...)

📦 Building an EXE (Optional)
You can package the project into a standalone EXE with PyInstaller:
pyinstaller --onefile --icon=icon.ico --add-data "icon.png;." main.py
This will generate dist/main.exe.
Note:
Windows Defender and other antivirus may flag unsigned EXEs as suspicious. You can ignore this (or build locally from source) if you trust the code.

📄 License
This project is released under the MIT License.

💬 Contact
If you are the BetterDiscord team, Discord, or another relevant party and would like this repository removed or modified, please open an issue or contact me directly.

🙏 Acknowledgments

BetterDiscord

Discord

PyInstaller

pystray
