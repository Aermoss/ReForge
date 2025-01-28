import reforge

from reforge.math import Vector2, Vector3, Vector4

class Window:
    def __init__(self, title: str, width: int, height: int, backgroundColor: Vector4 = Vector4(0.0, 0.0, 0.0, 255.0)) -> None:
        self.title, self.width, self.height, self.backgroundColor = title, width, height, backgroundColor
        self.context, self.uuid, self.terminated = reforge.getContextCurrent(), None, False
        self._window = reforge.api.Window(title, width, height)
        self.size = Vector2(self.width, self.height)
        self.input = reforge.Input(self)

    def eventHandler(self, event: object) -> None:
        if event.type == reforge.api.EventType.WindowClosed:
            if event.windowId is None or (event.windowId is not None and event.windowId == self._window._windowID): self.terminate()
        else: self.input.eventHandler(event)

    def terminate(self) -> None:
        if self.uuid != None:
            self.context.removeWindow(self.uuid)

        self._window.terminate()
        self.terminated = True