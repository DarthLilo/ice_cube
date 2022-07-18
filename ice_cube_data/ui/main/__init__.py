import importlib

from . import bone_layers
from . import general_settings


files_list = (
    bone_layers,
    general_settings,
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

