import subprocess
import time


def start_chrome():
    """Launch Google Chrome with remote debugging enabled."""
    cmd = [
        "google-chrome",
        "--remote-debugging-port=9223",
        f"--user-data-dir=$HOME/chrome-debug"
    ]
    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)
