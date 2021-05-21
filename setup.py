import sys
import  os
from cx_Freeze import setup, Executable

files = ["icon.ico",'modules/']

target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico",
)

setup(
    name = "PyIOT",
    version = "3.0",
    description = "IOT-MQTT",
    author = "Ivan S. Diaz",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)
