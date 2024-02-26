import reforge, sdl2, sdl2.ext, ctypes, uuid

from reforge.window import Window
from reforge.math import Vector2
from reforge.logger import LogLevel, Logger

class Context:
    def __init__(self, logLevel = LogLevel.Info) -> None:
        self.terminated, self.windows = False, {}
        self.displaySize = Vector2(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
        self._context, self.logger = reforge.api.Context(), Logger(logLevel)
        self.eventHandler, self.event = reforge.api.EventHandler(), reforge.api.Event()

    def makeContextCurrent(self) -> None:
        reforge.setContextCurrent(self)

    def pollEvents(self) -> None:
        while self.eventHandler.pollEvents(self.event):
            for _uuid in self.windows.copy():
                self.windows[_uuid].eventHandler(self.event)

        for _uuid in self.windows.copy():
            self.windows[_uuid].input.onUpdate()

        if len(self.windows) == 0:
            self.terminate()

    def registerWindow(self, window: Window) -> None:
        _uuid = uuid.uuid4()
        while _uuid in self.windows: _uuid = uuid.uuid4()
        window.context, window.uuid = self, _uuid
        self.windows[_uuid] = window
        return _uuid
    
    def removeWindow(self, _uuid: uuid.UUID) -> None:
        window = self.windows[_uuid]
        window.context, window.uuid = None, None
        del self.windows[_uuid]

    def isTerminated(self) -> None:
        return self.terminated
        
    def terminate(self, terminateWindows: bool = True) -> None:
        if self._context is None: return
        self.terminated = True

        for _uuid in (self.windows.copy() if terminateWindows else []):
            self.windows[_uuid].terminate()
            self.removeWindow(_uuid)

        if reforge.getContextCurrent() == self:
            reforge.setContextCurrent(None)

        self._context.terminate()
        self._context = None