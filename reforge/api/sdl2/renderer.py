import reforge.api, sdl2, ctypes

from reforge.math import Vector2, Vector3, Vector4

class Renderer:
    def __init__(self, window, vsync = False) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.window, self.vsync = window, vsync
        flags = sdl2.SDL_RENDERER_ACCELERATED
        if vsync: flags |= sdl2.SDL_RENDERER_PRESENTVSYNC
        self._renderer = sdl2.SDL_CreateRenderer(self.window._window, -1, sdl2.SDL_RENDERER_ACCELERATED)

    def setDrawColor(self, color: Vector4) -> None:
        sdl2.SDL_SetRenderDrawColor(self._renderer, *[int(i) for i in color.get()])

    def setViewport(self, x: int, y: int, width: int, height: int) -> None:
        sdl2.SDL_RenderSetViewport(self._renderer, sdl2.SDL_Rect(int(x), int(y), int(width), int(height)))

    def setVSync(self, vsync: bool) -> None:
        self.vsync = vsync
        sdl2.SDL_RenderSetVSync(self._renderer, 1 if vsync else 0)

    def setScale(self, x: float, y: float) -> None:
        sdl2.SDL_RenderSetScale(self._renderer, x, y)

    def drawRect(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderDrawRect(self._renderer, sdl2.SDL_Rect(*position.getInt(), *scale.getInt()))

    def drawRectF(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderDrawRectF(self._renderer, sdl2.SDL_FRect(*position.get(), *scale.get()))

    def fillRect(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderFillRect(self._renderer, sdl2.SDL_Rect(*position.getInt(), *scale.getInt()))

    def fillRectF(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderFillRectF(self._renderer, sdl2.SDL_FRect(*position.get(), *scale.get()))

    def createTextureFromSurface(self, surface) -> sdl2.SDL_Texture:
        return sdl2.SDL_CreateTextureFromSurface(self._renderer, surface)
    
    def renderTexture(self, texture, position: Vector2, angle: float = 0.0, center: Vector2 = None) -> None:
        width, height = ctypes.c_int(0), ctypes.c_int(0)
        sdl2.SDL_QueryTexture(texture, None, None, ctypes.byref(width), ctypes.byref(height))
        if center == None: center = Vector2(width.value / 2, height.value / 2)
        sdl2.SDL_RenderCopyEx(self._renderer, texture, None, \
            sdl2.SDL_Rect(*position.getInt(), width.value, height.value), angle, sdl2.SDL_Point(*center.getInt()), sdl2.SDL_FLIP_NONE)
    
    def renderSurface(self, surface, position: Vector2, angle: float = 0.0, center: Vector2 = None) -> None:
        texture = self.createTextureFromSurface(surface._surface.surface)
        self.renderTexture(texture, position, angle, center)
        sdl2.SDL_DestroyTexture(texture)

    def clear(self, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl2.SDL_RenderClear(self._renderer)

    def present(self) -> None:
        sdl2.SDL_RenderPresent(self._renderer)

    def terminate(self) -> None:
        ...