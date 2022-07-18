import importlib

from . import main_operators
from . import append
from . import os_management
from . import parenting
from . import web




#Reload
importlib.reload(main_operators)
importlib.reload(append)
importlib.reload(os_management)
importlib.reload(parenting)
importlib.reload(web)


def register():
    main_operators.register()
    append.register()
    os_management.register()
    parenting.register()
    web.register()

def unregister():
    main_operators.unregister()
    append.unregister()
    os_management.unregister()
    parenting.unregister()
    web.unregister()

