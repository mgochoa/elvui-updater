# build_exe.py
from PyInstaller.__main__ import run

if __name__ == "__main__":
    # Replace 'myapp.py' with the actual filename of your Tkinter app script
    script_file = 'main.py'
    run(['--onefile', script_file])
