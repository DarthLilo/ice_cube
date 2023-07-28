import importlib

from . import style
from . import controls
from . import materials
from . import advanced

files_list = (
    style,
    controls,
    materials,
    advanced,
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

