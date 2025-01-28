import reforge.api.instanceHandler, sdl3

class Window:
    def __init__(self, title: str, width: int, height: int) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.title, self.width, self.height = title, width, height
        self._window = sdl3.SDL_CreateWindow(title.encode(), width, height, 0)
        self._windowID = sdl3.SDL_GetWindowID(self._window)

    def terminate(self) -> None:
        sdl3.SDL_DestroyWindow(self._window)