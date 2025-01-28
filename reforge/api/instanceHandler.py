import os, sys, inspect, importlib

def addInstance(name, instance) -> None:
    getattr(sys.modules[".".join(name.split(".")[:-1])], "instances").append(instance)

def initInstanceHandler(name) -> None:
    setattr(sys.modules[name], "instances", [])

def terminateInstanceHandler(name) -> None:
    if not hasattr(sys.modules[name], "instances"): return
    instances = getattr(sys.modules[name], "instances")
    for i in instances[::-1]: i.terminate()
    delattr(sys.modules[name], "instances")

def importAllFilesInDirectory(file, name) -> None:
    for i in os.listdir(os.path.dirname(file)):
        if i.startswith("_") or not i.endswith(".py"): continue
        else: module = importlib.import_module(f"reforge.api.{os.path.split(os.path.dirname(file))[1]}.{os.path.splitext(i)[0]}")

        for j in dir(module):
            if j.startswith("_") or not inspect.isclass(getattr(module, j)) or not j[0].isupper(): continue
            setattr(sys.modules[name], j, getattr(module, j))