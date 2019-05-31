#!/usr/local/bin/python3
# gunicorn story:app to run the server
# Kino Rose
# NierPixel story book api

import falcon
import sys, os, subprocess
import json
from typing import List
import time

system_type:str = sys.platform

def get_story_json(file_name) -> None:
    executable_path:str = ""
    result:str = ""
    if system_type == "linux":
        print("Linux Platform Code")
    elif system_type == "win32":
        print("Windows Specific Code Runner")
    elif system_type == "darwin":
        print("Mac OS System Runner")
        executable_path = "./inklecate_mac/inklecate"
    subprocess.run([executable_path, file_name])
    json_file = open(file_name + ".json", encoding="utf8")
    file_contents = json_file.read()
    json_file.close()
    return file_contents



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