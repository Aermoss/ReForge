__version__ = "0.1.1"

import atexit, sys

sys.dont_write_bytecode = True

from typing import Any

entryPoints = ["main", "reforgeMain", "entry", "reforgeEntry"] + ["WinMain"] if sys.platform == "win32" else []
applicationCreations = ["createApplication", "reforgeCreateApplication"]
exitSuccess, exitFailure = range(2)

import reforge.api as api

def blacklistEntry(func):
    entryPoints.remove(func.__name__)

@atexit.register
def exitHandler() -> int:
    __main__ = __import__("__main__")

    for i in entryPoints:
        if not hasattr(__main__, i): continue
        if not api.setCurrentAPI(os.environ.get("REFORGE_API")):
            api.apiLog(api.apiLogType.FatalError, "invalid API specified in environment variable!", terminate = True)

        if len(api.initAPI()) == 0:
            api.apiLog(api.apiLogType.FatalError, "no API was initialized!", terminate = True)

        exitCode = getattr(__main__, i)(len(sys.argv), sys.argv)
        api.terminateAPI()
        return exitCode
        
    for i in applicationCreations:
        if not hasattr(__main__, i): continue
        os._exit(getattr(__main__, i)(len(sys.argv), sys.argv).run())

from reforge.context import *

contextCurrent = None

def setContextCurrent(context) -> None:
    global contextCurrent
    contextCurrent = context

def getContextCurrent() -> Context:
    return contextCurrent

applicationInstance = None

from reforge.math import *
from reforge.surface import *
from reforge.renderer import *
from reforge.font import *
from reforge.scene import *
from reforge.entity import *
from reforge.components import *
from reforge.logger import *
from reforge.input import *
from reforge.color import *
from reforge.window import *
from reforge.utils import *
from reforge.application import *