import importlib

from . import inventory_system
from . import skin_downloader
from . import search_system

#Reload
importlib.reload(inventory_system)
importlib.reload(skin_downloader)
importlib.reload(search_system)


def register():
    inventory_system.register()
    skin_downloader.register()
    search_system.register()

def unregister():
    inventory_system.unregister()
    skin_downloader.unregister()
    search_system.unregister()

