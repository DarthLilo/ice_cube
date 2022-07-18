import importlib

from . import dlc_ui
from . import downloads
from . import parenting
from . import adv_misc


files_list = (
    dlc_ui,
    downloads,
    parenting,
    adv_misc
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

