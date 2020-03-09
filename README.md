# Blender Nexss PROGRAMMER package

You can render results in **Blender** directly from **nexss PROGRAMMER**.

## Start Scripting in Blender

- Enable Python Tooltips -> Edit -> Preferences -> Interface -> [Display] Python Tooltip
- Info Panel shows history of commands executed
- CTRL + T - shows properties
- ALT + P run Script on active text-editor

## Examples

```sh
nexss .\my.py --nxsCompiler="blender --background"
```

## Links

[2.8 vs 2.7](https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Scene_and_Object_API)

## Parameters

- width
- height
- objectName - Name of object in the scene to modify
- renderData - String which contains data to render, otherwise it contains datetime stamp.
- renderFilename
- colorMode [‘BW’, ‘RGB’, ‘RGBA’]
- compression (0-100)

more here: [Blender image format settings](https://docs.blender.org/api/blender_python_api_master/bpy.types.ImageFormatSettings.html?highlight=compression#bpy.types.ImageFormatSettings.compression)

## Create custom Scene

1. Create new scene and save it as eg. myfile.blend
2. Create eg. Text Object and rename it to NEXSSEDIT or you need to pass parameter of objectName.

## Config file

To run your python script in blender make compiler option with scene file: blender eg

```yml
files:
  - name: src/yourScript.py
    compiler: blender yourBlenderScene.blend --background
```

## Modify code to your needs

nore here: <https://github.com/nexssp/cli/blob/master/nexss-package/help.md>

```sh
# This will copy package to your current folder.
# You can use it like: nexss Blender (the same as global package)
# Now you can adjust the copied code to your needs.
nexss pkg add Blender --copyPackage --saveNexss --forceNexss
```

## Credits

Languages/Technologies used for this Nexss PROGRAMMER package:

- NodeJS
- Python
- Blender

## Tips and Tricks

Open `info panel` to display operations by doing changes in the blender. You can paste them to the script.

## Scripting in Blender

### Snippets

Execute script

```sh
# nexss
# NORE: Blender render does not allow for custom arguments (-- but for now it is not implemented in nexss PROGRAMMER), you need to pass it through pipe eg. or in _nexss.yml in data section.

echo {"ObjectName": "NexssEdit"} | nexss Blender

# In Blender
blender --background --python myscript.py
blender myscene.blend --background --python myscript.py
```

```py
import bpy
import os

filename = os.path.join(os.path.dirname(bpy.data.filepath), "myscript.py")
exec(compile(open(filename).read(), filename, 'exec'))
```

Loading Script as module

```py
import myscript
import importlib

importlib.reload(myscript)
myscript.main()
```

Adding search path

```py
import sys
import os
import bpy

blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

import myscript
import importlib
importlib.reload(myscript)
myscript.main()
```

## Blender Related

### Useful Links

[Blender Nation - Blender Scripts](https://www.blendernation.com/category/blender/python-scripts/)  
<https://docs.blender.org/api/current/info_tips_and_tricks.html>
[HDRI Heaven](https://hdrihaven.com/)  
<https://texture.ninja>  
[Supercharge Blender 2.8](https://www.youtube.com/watch?v=yWnp8he1oq4)

#### Useful shortcuts

[Blender Hot Keys References](https://download.blender.org/documentation/BlenderHotkeyReference.pdf)  
CTRL + ALT + SHIFT + C -> Cursor  
Shift + S - SNAP - cursor to selection etc

Bevel Edge - CTRL + B, OR use vertex group - + and Assign, then add modifier  
Bevel Vertex - CTRL + SHIFT + B

Collections  
M - Move to collection  
NUM+, NUM- - shows/shrink collections menu

SHIFT + SPACE special menu for each functionality
. -
, -

- U - for unwraping (while face selected/edit mode) - make island margin 0.3!

- TAB - Edit mode
- CTRL + TAB - Vertext mode, Sculpt mode, Texture pain, Vertex Paint
- CTRL + H - Hook Object Options
- 1,2,3 - Vertices, Edge and Face mode while editing
- / - show only selected object
- K - Knife tool
- Q - quick favourites
- T - Toolbar
- N - Properties
- ` - change view menu (camera, top,left,right...)
- Z - change view menu
- SHIFT + D - duplicate
- ALT + D - duplicate linked.
- SHIFT + Z - Wireframe mode
- ALT + Z \_ XRAY mode
- SHIFT + R - Repeat last action
- CTRL + R - edge loop
- ALT + R - Reset rotation
- SHIFT + SPACE - Play animation
- CTRL + SPACE - Full screen of current
- CTRL + ALT + NUM0 - snam the view to the camera.(also select border and g for moving)
- ALT + A - scale faces ??? (on skin modifier)

CTRL + M+X+X - flip camera

### Interesting add ons for Blender

#### Node Wrangler

Adds new shortcuts in the node view

- CTRL + T - adds texture mapping nodes
- CTRL + X - remove node and keep connections
- CTRL + SHIFT + CLICK - preview node

#### Loop Tools

right click on edit -> loop tools

#### ArchiMesh -> Add -> Mesh -> Archimesh

#### Simplify Curves

For animation graph - simplyfy curves / smoother anim
