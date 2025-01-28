import os, sys, inspect, warnings

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

if os.environ.get("PYSDL2_DLL_PATH") is None:
    import sdl2dll

from reforge.api.logger import *
from reforge.api.instanceHandler import *
from reforge.api.event import *

from typing import Any, Union, Tuple, List, Dict

currentAPI = None
initializedClasses = []
apiModules = {}

for i in os.listdir(os.path.dirname(__file__)):
    if os.path.isdir(os.path.join(os.path.dirname(__file__), i)):
        apiModules[i.lower()] = __import__("reforge.api." + i, fromlist = ["reforge", "api"])

def initAPI() -> List[str]:
    initializedClasses.clear()
    apiModule = getAPIModule()
    if apiModule is not None: initInstanceHandler(apiModule.__name__)
    module, members = sys.modules[__name__], []

    for i in [dir(j) for j in list(apiModules.values())]:
        members.append(set(i))

    for i in list(set.intersection(*members)):
        if i.startswith("_") or (False in [inspect.isclass(getattr(j, i)) for j in list(apiModules.values())]) or not i[0].isupper(): continue
        setattr(module, i, getattr(apiModule, i) if apiModule is not None else None)
        if apiModule is not None: initializedClasses.append(i)

    import reforge, reforge.input

    for i in ["Key", "Button"]:
        setattr(reforge, i, getattr(module, i) if apiModule is not None else None)

    return initializedClasses

def terminateAPI() -> None:
    apiModule = getAPIModule()
    terminateInstanceHandler(apiModule.__name__)
    module = sys.modules[__name__]
    
    for i in initializedClasses:
        delattr(module, i)

    import reforge, reforge.input

    for i in ["Key", "Button"]:
        delattr(reforge, i)

def setCurrentAPI(api: str) -> None:
    global currentAPI
    isInitialized = len(initializedClasses) != 0
    if isInitialized: terminateAPI()
    currentAPI = api.lower() if api.lower() in list(apiModules.keys()) else None
    if isInitialized: initAPI()
    return not (currentAPI is None and api is not None)

def getCurrentAPI() -> int:
    return currentAPI

def getAPIModule() -> object:
    if getCurrentAPI() not in apiModules: return None
    return apiModules.get(getCurrentAPI())

if len(initAPI()) != 0:
    apiLog(apiLogType.FatalError, "something went wrong while initializing the API!", terminate = True)