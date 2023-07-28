import importlib

from . import old_dlc_ui
from . import old_downloads
from . import old_parenting
from . import old_adv_misc


files_list = (
    old_dlc_ui,
    old_downloads,
    old_parenting,
    old_adv_misc
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

