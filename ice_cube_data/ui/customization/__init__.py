import importlib

from . import old_custom_general
from . import old_mesh
from . import old_misc


files_list = (
    old_custom_general,
    old_mesh,
    old_misc,
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

