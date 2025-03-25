import reforge, os

def joinPath(*args: str) -> str:
    return os.path.abspath(os.path.join(*args)).replace("\\", "/")

def splitPath(path: str) -> tuple[str, str]:
    return [i.replace("\\", "/") for i in os.path.split(path)]

def splitExt(path: str) -> tuple[str, str]:
    return [i.replace("\\", "/") for i in os.path.splitext(path)]

def dirName(path: str) -> str:
    return os.path.dirname(path).replace("\\", "/")

def absPath(path: str) -> str:
    return os.path.abspath(path).replace("\\", "/")