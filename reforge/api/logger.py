import sys

class apiLogType:
    FatalError, Error, Warning, Info = "fatal error", "error", "warning", "info"

def apiLog(type, message, terminate = False) -> None:
    print(f"reforge: api: {type}: {message}")
    if terminate: sys.exit(1)