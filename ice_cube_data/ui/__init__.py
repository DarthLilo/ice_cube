import importlib

from . import advanced
from . import customization
from . import main
from . import materials


files_list = (
    advanced,
    customization,
    main,
    materials,
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

