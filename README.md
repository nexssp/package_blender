# Blender Nexss Module

You can render you results directly from nexss PROGRAMMER in blender.

To run script in blender make compiler option eg

```yml
files:
  - name: src/my.py
    compiler: blender nexsstest.blend --background
```

## Tips and Tricks

Open `info panel` to display operations by doing changes in the blender. You can paste them to the script.

## Useful Links

[Blender Nation - Blender Scripts](https://www.blendernation.com/category/blender/python-scripts/)
(https://docs.blender.org/api/current/info_tips_and_tricks.html)
[HDRI Heaven](https://hdrihaven.com/)
<https://texture.ninja>
[Supercharge Blender 2.8](https://www.youtube.com/watch?v=yWnp8he1oq4)

## Useful shortcuts

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

## Interesting add ons for Blender

### Node Wrangler

Adds new shortcuts in the node view

- CTRL + T - adds texture mapping nodes
- CTRL + X - remove node and keep connections
- CTRL + SHIFT + CLICK - preview node

### Loop Tools

right click on edit -> loop tools

### ArchiMesh -> Add -> Mesh -> Archimesh

### Simplify Curves

For animation graph - simplyfy curves / smoother anim

## Scripting in Blender

### Snippets

Execute script

```sh
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
