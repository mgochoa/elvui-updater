# build_exe.py
from PyInstaller.__main__ import run
import os

if __name__ == "__main__":
    # Replace 'myapp.py' with the actual filename of your Tkinter app script
    script_file = 'gui.py'

    if not os.path.exists('gui.spec'):

        run(["-y", "--log-level=DEBUG", "--add-data=./assets:assets", script_file])
    else:
        run(['-y', 'gui.spec'])
