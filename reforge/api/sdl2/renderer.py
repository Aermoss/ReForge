import reforge.api.tools, reforge.api.event, reforge.math, sdl2

class Renderer:
    def __init__(self, window, vsync = False) -> None:
        reforge.api.tools.addInstance(__name__, self)
        self.window, self.vsync = window, vsync
        flags = sdl2.SDL_RENDERER_ACCELERATED
        if vsync: flags |= sdl2.SDL_RENDERER_PRESENTVSYNC
        self._renderer = sdl2.SDL_CreateRenderer(self.window._window, -1, sdl2.SDL_RENDERER_ACCELERATED)

    def setDrawColor(self, color: reforge.math.Vector4) -> None:
        sdl2.SDL_SetRenderDrawColor(self._renderer, *[int(i) for i in color.get()])

    def setViewport(self, x: int, y: int, width: int, height: int) -> None:
        sdl2.SDL_RenderSetViewport(self._renderer, sdl2.SDL_Rect(int(x), int(y), int(width), int(height)))

    def setVSync(self, vsync: bool) -> None:
        self.vsync = vsync
        sdl2.SDL_RenderSetVSync(self._renderer, 1 if vsync else 0)

    def setScale(self, x: float, y: float) -> None:
        sdl2.SDL_RenderSetScale(self._renderer, x, y)

    def drawRect(self, x: int, y: int, width: int, height: int, color: reforge.math.Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderDrawRect(self._renderer, sdl2.SDL_Rect(int(x), int(y), int(width), int(height)))

    def drawRectF(self, x: float, y: float, width: float, height: float, color: reforge.math.Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderDrawRectF(self._renderer, sdl2.SDL_FRect(float(x), float(y), float(width), float(height)))

    def fillRect(self, x: int, y: int, width: int, height: int, color: reforge.math.Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderFillRect(self._renderer, sdl2.SDL_Rect(int(x), int(y), int(width), int(height)))

    def fillRectF(self, x: float, y: float, width: float, height: float, color: reforge.math.Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderFillRectF(self._renderer, sdl2.SDL_FRect(float(x), float(y), float(width), float(height)))

    def clear(self, color: reforge.math.Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderClear(self._renderer)

    def present(self) -> None:
        sdl2.SDL_RenderPresent(self._renderer)

    def terminate(self) -> None:
        ...