import importlib

from . import custom_general
from . import mesh
from . import misc


files_list = (
    custom_general,
    mesh,
    misc,
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

