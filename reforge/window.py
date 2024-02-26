import reforge

class Window:
    def __init__(self, title: str, width: int, height: int) -> None:
        self.title, self.width, self.height, self.context, self.uuid, self.terminated = title, width, height, reforge.getContextCurrent(), None, False
        self._window = reforge.api.Window(title, width, height)
        self.size = reforge.Vector2(self.width, self.height)
        self.input = reforge.Input(self)

    def eventHandler(self, event: object) -> None:
        if event.type == reforge.api.EventType.WindowClosed:
            if event.windowID is None or (event.windowID is not None and event.windowID == self._window._windowID): self.terminate()
        else: self.input.eventHandler(event)

    def terminate(self) -> None:
        if self.uuid != None:
            self.context.removeWindow(self.uuid)

        self._window.terminate()
        self.terminated = True