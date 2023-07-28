import importlib

from . import old_bone_layers
from . import old_general_settings


files_list = (
    old_bone_layers,
    old_general_settings,
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

