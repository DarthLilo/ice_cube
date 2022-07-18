import importlib

from . import inventory_system
from . import skin_downloader

#Reload
importlib.reload(inventory_system)
importlib.reload(skin_downloader)


def register():
    inventory_system.register()
    skin_downloader.register()

def unregister():
    inventory_system.unregister()
    skin_downloader.unregister()

