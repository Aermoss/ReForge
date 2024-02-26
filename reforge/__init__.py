import atexit, sys

sys.dont_write_bytecode = True

from typing import List

entryPoints = ["WinMain", "reforgeMain", "main", "reforgeEntry", "entry"]
exitSuccess, exitFailure = range(2)

import reforge.api as api

def blacklistEntry(func):
    entryPoints.remove(func.__name__)

@atexit.register
def exitHandler() -> int:
    __main__ = __import__("__main__")

    for i in entryPoints:
        if hasattr(__main__, i):
            if len(api.initAPI()) == 0: print("NO API WAS INITIALIZED!")
            result = getattr(__main__, i)(len(sys.argv), sys.argv)
            api.terminateAPI()
            return result

from reforge.context import *

contextCurrent = None

def setContextCurrent(context) -> None:
    global contextCurrent
    contextCurrent = context

def getContextCurrent() -> Context:
    return contextCurrent

from reforge.renderer import *
from reforge.scene import *
from reforge.entity import *
from reforge.components import *
from reforge.logger import *
from reforge.window import *
from reforge.input import *
from reforge.math import *