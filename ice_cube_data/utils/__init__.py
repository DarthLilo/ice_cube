import importlib

from . import file_manage
from . import general_func
from . import selectors
from . import ui_tools
from . import web_tools

#Reload
importlib.reload(file_manage)
importlib.reload(general_func)
importlib.reload(selectors)
importlib.reload(ui_tools)
importlib.reload(web_tools)
importlib.reload(importlib)


def register():
    file_manage.register()
    general_func.register()
    selectors.register()
    ui_tools.register()
    web_tools.register()

def unregister():
    file_manage.unregister()
    general_func.unregister()
    selectors.unregister()
    ui_tools.unregister()
    web_tools.unregister()

