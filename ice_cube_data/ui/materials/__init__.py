import importlib

from . import old_eye_material
from . import old_misc_material
from . import old_skin_material

files_list = (
    old_eye_material,
    old_misc_material,
    old_skin_material,
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

