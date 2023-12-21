# build_exe.py
from PyInstaller.__main__ import run

if __name__ == "__main__":
    script_file = 'gui.py'

    run(["-y", "--noconsole", "--onefile", "-n ElvuiUpdater", "--add-data=./assets:assets", script_file])
