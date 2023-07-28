import importlib

from . import advanced
from . import customization
from . import main
from . import materials
from . import new_ui


files_list = (
    advanced,
    customization,
    main,
    materials,
    new_ui,
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

