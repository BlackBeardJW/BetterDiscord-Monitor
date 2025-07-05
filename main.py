# main.py
import threading
from monitor import monitor_loop
from tray import create_tray_icon

def main():
    t = threading.Thread(target=monitor_loop, daemon=True)
    t.start()
    create_tray_icon(t)

if __name__ == "__main__":
    main()
