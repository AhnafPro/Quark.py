import os
import sys

add_data = f"web{os.pathsep}web"
command = [
    sys.executable,
    "-m",
    "PyInstaller",
    "--onedir",
    "--windowed",
    "--clean",
    "--strip",
    "--add-data",
    add_data,
    "main.py"
]

command_str = " ".join(command)

print("Building the app...")
os.system(command_str)
print("Done! Check the dist folder")