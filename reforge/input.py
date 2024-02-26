import reforge, sdl2, sdl2.ext, pygame

class Input:
    def __init__(self, window: reforge.Window) -> None:
        self.window = window
        self._input = reforge.api.Input(window._window)
        self.keyboard, self.mouse = self._input.keyboard, self._input.mouse

    def onUpdate(self) -> None:
        self._input.update()

    def eventHandler(self, event: object) -> None:
        self._input.eventHandler(event)

    def terminate(self):
        self._input.terminate()