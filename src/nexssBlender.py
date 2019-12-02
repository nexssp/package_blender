# Nexss PROGRAMMER 2.0.0 - Python3
# Render results in Blender 3D

from datetime import datetime
from bpy import context
import bpy
import platform
import json
import sys
import os
from pprint import pprint


def fileformat(i):
    switcher = {
        '.jpg': 'JPEG',
        '.jpeg': 'JPEG',
        '.png': 'PNG',
        '.bmp': 'BMP',
        '.tga': 'TARGA',  # TARGA_RAW
        '.tiff': 'TIFF',  # TARGA_RAW
        '.avi': 'AVI_RAW',  # AVI_JPEG
        '.mp4': 'FFMPEG'
    }
    return switcher.get(i, "Invalid fileformat, use extensions: .jpg, .png, .bmp, .tga, .avi, mp4")


# STDIN
NexssStdin = sys.stdin.read()

parsedJson = json.loads(NexssStdin)

scene = bpy.context.scene
# foo_objs = [obj for obj in scene.objects if obj.name.startswith("foo")]
# Active object / or last added object
# ob = scene.objects.active

pprint(bpy.context.scene.objects)


editObjectName = "NEXSSEDIT"
if "objectName" in parsedJson.keys():
    editObjectName = parsedJson["objectName"]

if "renderBody" in parsedJson.keys():
    bpy.data.objects[editObjectName].data.body = str(parsedJson["renderBody"])
else:
    now = datetime.now()
    bpy.data.objects[editObjectName].data.body = now.strftime(
        "%d/%m/%Y %H:%M:%S")


renderFilename = "myfile.jpg"
if "renderFilename" in parsedJson.keys():
    renderFilename = parsedJson["renderFilename"]

filename, file_extension = os.path.splitext(renderFilename)
file_format = fileformat(file_extension)
bpy.context.scene.render.image_settings.file_format = file_format

parsedJson["file"] = os.path.join(parsedJson["cwd"], renderFilename)
bpy.data.scenes['Scene'].render.filepath = parsedJson["file"]

# Render Resolution
width = 320
if "width" in parsedJson.keys():
    width = parsedJson["width"]
    if not isinstance(width, int):
        raise NameError('width must be a number')


bpy.context.scene.render.resolution_x = width

height = 280
if "height" in parsedJson.keys():
    height = parsedJson["height"]
    if not isinstance(height, int):
        raise NameError('height must be a number')

bpy.context.scene.render.resolution_y = height

color_mode = "RGB"
if "colorMode" in parsedJson.keys():
    color_mode = parsedJson["colorMode"]

bpy.context.scene.render.image_settings.color_mode = color_mode

compression = 90
if "compression" in parsedJson.keys():
    compression = parsedJson["compression"]
bpy.context.scene.render.image_settings.compression = compression


if file_format == "AVI_RAW":
    bpy.ops.render.render(animation=True)
else:
    bpy.ops.render.render(write_still=True)
# bpy.ops.render.render(use_viewport = True, write_still=True)

NexssStdout = json.JSONEncoder().encode(parsedJson)
# STDOUT
sys.stdout.write(NexssStdout)
