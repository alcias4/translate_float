from pynput import keyboard
import subprocess
from pathlib import Path

def open_app() -> None:
    ROOT = Path(__file__).resolve().parent.parent

    APP_PATH = ROOT / "dist" / "Translator_camilo" / "Translator_camilo.exe"
    if not APP_PATH.is_file():
        print(f"Executable not found: {APP_PATH}")
        return

    subprocess.Popen(
        [str(APP_PATH)],
        cwd=APP_PATH.parent
    )



def command_keys():
    with keyboard.GlobalHotKeys({
        "<cmd>+y": open_app
    }) as listener:
        listener.join()


if __name__ == "__main__":
    command_keys()