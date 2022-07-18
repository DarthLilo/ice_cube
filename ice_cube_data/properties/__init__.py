import importlib

from . import properties


#Reload
importlib.reload(properties)


def register():
    properties.register()

def unregister():
    properties.unregister()

