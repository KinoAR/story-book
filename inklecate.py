#!/usr/local/bin/python3
import sys
import os
import subprocess
import time
import datetime
import json
from typing import List
# Inklecate Runner for system level use
# Kino Rose - NierPixel.com

def run_story(platform, story_arg):
    print(story_arg)
    print("Ran story at", datetime.datetime.now())
    absolute_path = (os.path.abspath(story_arg))
    if os.path.exists(absolute_path + ".json"):
        with open(absolute_path, 'r') as file:
            return file.read()
    else:
        return subprocess.run([platform, '-p', absolute_path])

args:List[str] = sys.argv[1:]

system_type:str = sys.platform
normal_process = []

if system_type == "linux":
    print("Linux Runner")
    run_story('mono ./iinklecate_windows_and_linux/inklecate.exe', args[0])
elif system_type == "win32":
    print("Windows Runner")
    run_story('./inklecate_windows_and_linux/inklecate.exe', args[0])
elif system_type == "darwin":
    print("Mac Runner")
    run_story('./inklecate_mac/inklecate', args[0])
