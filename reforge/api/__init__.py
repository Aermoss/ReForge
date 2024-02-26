import os, sys, inspect, warnings

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

if os.environ.get("PYSDL2_DLL_PATH") is None:
    import sdl2dll

from reforge.api.tools import *
from reforge.api.event import *

from typing import List

if "REFORGE_API" not in os.environ:
    os.environ["REFORGE_API"] = "sdl2"

NULL, PYGAME, SDL2 = range(-1, 2)
currentAPI = SDL2 if os.environ.get("REFORGE_API").upper() == "SDL2" else PYGAME

initializedClasses = []

def initAPI() -> List[str]:
    initializedClasses.clear()
    apiModule = getAPIModule()
    initInstanceHandler(apiModule.__name__)
    module = sys.modules[__name__]

    for i in list(set(dir(pygame)) & set(dir(sdl2))):
        if i.startswith("_") or (False in [inspect.isclass(getattr(j, i)) for j in [pygame, sdl2]]) or not i[0].isupper(): continue
        setattr(module, i, getattr(apiModule, i))
        initializedClasses.append(i)

    import reforge, reforge.input

    for i in ["Key", "Button"]:
        setattr(reforge, i, getattr(module, i))
        
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

def setCurrentAPI(api: int) -> None:
    global currentAPI
    if currentAPI != NULL: terminateAPI()
    currentAPI = api
    if currentAPI != NULL: initAPI()

def getCurrentAPI() -> int:
    return currentAPI

def getAPIModule() -> object:
    return {SDL2: sdl2, PYGAME: pygame}[getCurrentAPI()]

import reforge.api.pygame as pygame
import reforge.api.sdl2 as sdl2