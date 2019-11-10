# Nexss PROGRAMMER 2.0.0 - Python3
# Default template for JSON Data

import bpy
import platform
import json
import sys
import os
from pprint import pprint

# STDIN
NexssStdin = sys.stdin.read()

parsedJson = json.loads(NexssStdin)

from bpy import context
scene = bpy.context.scene
# foo_objs = [obj for obj in scene.objects if obj.name.startswith("foo")]
# Active object / or last added object
# ob = scene.objects.active

pprint(bpy.context.scene.objects)

from datetime import datetime
now = datetime.now()

editObjectName = "NEXSSEDIT"
if "objectName" in parsedJson.keys():
    editObjectName = parsedJson["objectName"]

bpy.data.objects[editObjectName].data.body = now.strftime("%d/%m/%Y %H:%M:%S")

parsedJson["file"] = os.path.join(parsedJson["cwd"],'test2.jpg')
bpy.data.scenes['Scene'].render.filepath = parsedJson["file"] 
bpy.context.scene.render.resolution_x = 320
bpy.context.scene.render.resolution_y = 280
bpy.context.scene.render.image_settings.file_format='JPEG'
bpy.ops.render.render(write_still=True)

# bpy.ops.render.render(use_viewport = True, write_still=True)

# bpy.data.objects['ObjectName'].select_set(state=True)
# pprint(globals())
# pprint(locals())
# print(D.objects());
# pprint("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
# pprint(parsedJson)
NexssStdout = json.JSONEncoder().encode(parsedJson)
# STDOUT
sys.stdout.write(NexssStdout)

def myf(text):
    bpy.data.objects['prompt'].data.body = text
