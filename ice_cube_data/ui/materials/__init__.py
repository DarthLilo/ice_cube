import importlib

from . import eye_material
from . import misc_material
from . import skin_material

files_list = (
    eye_material,
    misc_material,
    skin_material,
)

#Reload
for file in files_list:
    importlib.reload(file)


def register():
    for file in files_list:
        file.register()

def unregister():
    for file in files_list:
        file.unregister()

