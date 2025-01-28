import reforge

class LogLevel:
    Info, Warning, Error, FatalError, Null = range(5)

class Logger:
    def __init__(self, logLevel = LogLevel.Info) -> None:
        self.logLevel = logLevel

    def log(self, logLevel: LogLevel, message: str) -> None:
        if self.logLevel == LogLevel.Null:
            return None

        if logLevel >= self.logLevel:
            print("reforge: " + ["info", "warning", "error", "fatal error"][logLevel] + ": " + message)