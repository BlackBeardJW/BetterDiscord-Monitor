# monitor.py
import os
import time
import psutil
import subprocess
import logging
from datetime import datetime
from plyer import notification

# Setup logging to file
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

HEARTBEAT_FILE = os.path.join(
    os.environ["APPDATA"],
    "BetterDiscord",
    "plugins",
    "bd_heartbeat.txt"
)
INSTALLER_PATH = os.path.join(
    os.environ["APPDATA"],
    "BetterDiscord",
    "plugins",
    "BetterDiscord-Windows.exe"
)

DISCORD_PARENT_DIR = os.path.join(
    os.environ["LOCALAPPDATA"],
    "Discord"
)

STALE_THRESHOLD = 150  # 2.5 min
CHECK_INTERVAL = 30

def show_notification(title, message):
    try:
        notify_func = getattr(notification, "notify", None)
        if notify_func is not None and callable(notify_func):
            notify_func(
                title=title,
                message=message,
                timeout=5
            )
        else:
            logging.warning("Notification function is not available or is None.")
    except Exception as e:
        logging.warning(f"Notification failed: {e}")

def is_discord_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and 'Discord' in proc.info['name']:
            return True
    return False

def get_latest_app_folder():
    folders = [f for f in os.listdir(DISCORD_PARENT_DIR) if f.startswith("app-")]
    if not folders:
        return None
    return sorted(folders)[-1]

def monitor_loop():
    logging.info("Starting BetterDiscord monitor...")
    last_seen_app_folder = get_latest_app_folder()

    while True:
        if is_discord_running():
            current_app_folder = get_latest_app_folder()
            if current_app_folder != last_seen_app_folder:
                logging.info(f"Discord updated from {last_seen_app_folder} to {current_app_folder}")
                show_notification(
                    "BetterDiscord Watchdog",
                    "Discord updated - reinstalling BetterDiscord."
                )
                subprocess.Popen([INSTALLER_PATH], shell=True)
                last_seen_app_folder = current_app_folder

            if not os.path.exists(HEARTBEAT_FILE):
                logging.warning("Heartbeat file not found.")
            else:
                last_modified = os.path.getmtime(HEARTBEAT_FILE)
                age = time.time() - last_modified
                logging.info(f"Heartbeat age: {age:.1f}s")
                if age > STALE_THRESHOLD:
                    logging.warning("Heartbeat stale. Launching installer...")
                    show_notification(
                        "BetterDiscord Watchdog",
                        "Heartbeat stale. Launching installer."
                    )
                    subprocess.Popen([INSTALLER_PATH], shell=True)
        else:
            logging.info("Discord not running.")
        time.sleep(CHECK_INTERVAL)
