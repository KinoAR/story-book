#!/usr/local/bin/python3
import sys
import os
import subprocess
import multiprocessing
import time
from typing import List
# Inklecate Runner for system level use
# Kino Rose - NierPixel.com

def run_story(story_arg):
    print(story_arg)
    return subprocess.run(['./inklecate_mac/inklecate', '-p', (os.path.abspath(story_arg))])

args:List[str] = sys.argv[1:]

system_type:str = sys.platform
processes = []
normal_process = []

if system_type == "linux":
    print("Linux Platform Code")
elif system_type == "win32":
    print("Windows Specific Code Runner")
elif system_type == "darwin":
    print("Mac OS System Runner")
    #new_process = multiprocessing.Process(target=run_story, args=(args[0],))
    normal_process.append(run_story(args[0]))
    #new_process.start()
    #processes.append(new_process)
