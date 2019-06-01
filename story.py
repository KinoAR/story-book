#!/usr/local/bin/python3
# gunicorn story:app to run the server
# Kino Rose
# NierPixel story book api

import falcon
import sys, os, subprocess
import json
import datetime
from typing import List
import time

system_type:str = sys.platform
def read_file(file_name) -> str:
    with open(file_name, 'r', encoding="utf8") as file:
        return file.read()

def get_story_json(file_name) -> None:
    print("Ran story at", datetime.datetime.now())
    executable_path:str = ""
    json_path:str = file_name + ".json"
    result:str = ""
    if system_type == "linux":
        print("Linux Platform Code")
        executable_path = "mono ./iinklecate_windows_and_linux/inklecate.exe"
    elif system_type == "win32":
        print("Windows Specific Code Runner")
        executable_path = "./inklecate_windows_and_linux/inklecate.exe"
    elif system_type == "darwin":
        print("Mac OS System Runner")
        executable_path = "./inklecate_mac/inklecate"
    if os.path.exists(json_path):
        return read_file(json_path)
    else:
        subprocess.run([executable_path, file_name])
        return read_file(json_path)
    



# args:List[str] = sys.argv[1:]

# print(get_story_json(args[0]))

# Falcon REST API Endpoint
class StoryResource(object):
    def on_get(self, req, resp, story_name):
        """ Handles GET requests"""
        standard_path = "stories"
        resp.status = falcon.HTTP_200 # OK Status
        resp.body = get_story_json(os.path.join(standard_path, story_name + ".ink"))

app = falcon.API()
# Story Resource As Class Instance
story = StoryResource()
app.add_route("/story/{story_name}", story)