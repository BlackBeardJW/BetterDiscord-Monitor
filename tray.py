from pystray import MenuItem as Item, Icon
from PIL import Image
import subprocess
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource (works for dev and PyInstaller)"""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

def create_tray_icon(t):
    icon_path = resource_path("icon.png")
    image = Image.open(icon_path)

    icon = Icon(
        "BetterDiscord Monitor",
        icon=image,
        title="BetterDiscord Monitor",
        menu=(
            Item("Show Log Window", lambda icon, item: open_log_window()),
            Item("Exit", lambda icon, item: exit_app(icon))
        )
    )
    icon.run()

def open_log_window():
    log_path = os.path.join(os.getcwd(), "logs.txt")
    subprocess.Popen([
        "powershell.exe",
        "-NoExit",
        "-Command",
        f"Get-Content -Path '{log_path}' -Wait"
    ])

def exit_app(icon):
    icon.stop()
