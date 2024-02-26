import reforge.api.tools, sdl2

class Window:
    def __init__(self, title: str, width: int, height: int) -> None:
        reforge.api.tools.addInstance(__name__, self)
        self.title, self.width, self.height = title, width, height
        self._window = sdl2.SDL_CreateWindow(title.encode(), sdl2.SDL_WINDOWPOS_UNDEFINED, sdl2.SDL_WINDOWPOS_UNDEFINED, width, height, sdl2.SDL_WINDOW_SHOWN)
        self._windowID = sdl2.SDL_GetWindowID(self._window)

    def terminate(self) -> None:
        sdl2.SDL_DestroyWindow(self._window)