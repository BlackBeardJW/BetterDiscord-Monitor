# updater.py
import requests
import os

def download_latest_installer(dest_path):
    url = "https://github.com/BetterDiscord/Installer/releases/latest/download/BetterDiscord-Windows.exe"
    print("[Updater] Downloading latest installer...")
    r = requests.get(url)
    with open(dest_path, "wb") as f:
        f.write(r.content)
    print("[Updater] Download complete.")
