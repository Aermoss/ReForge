import reforge.api, sdl3, ctypes

from reforge.math import Vector2, Vector3, Vector4

class Renderer:
    def __init__(self, window, vsync = False) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.window, self.vsync = window, vsync
        self._renderer = sdl3.SDL_CreateRenderer(self.window._window, "opengl".encode())

    def setDrawColor(self, color: Vector4) -> None:
        sdl3.SDL_SetRenderDrawColor(self._renderer, *[int(i) for i in color.get()])

    def setViewport(self, x: int, y: int, width: int, height: int) -> None:
        sdl3.SDL_RenderSetViewport(self._renderer, sdl3.SDL_Rect(int(x), int(y), int(width), int(height)))

    def setVSync(self, vsync: bool) -> None:
        self.vsync = vsync
        sdl3.SDL_RenderSetVSync(self._renderer, 1 if vsync else 0)

    def setScale(self, x: float, y: float) -> None:
        sdl3.SDL_RenderSetScale(self._renderer, x, y)

    def drawRect(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl3.SDL_RenderRect(self._renderer, sdl3.SDL_FRect(*position.get(), *scale.get()))

    def drawRectF(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl3.SDL_RenderRect(self._renderer, sdl3.SDL_FRect(*position.get(), *scale.get()))

    def fillRect(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl3.SDL_RenderFillRect(self._renderer, sdl3.SDL_FRect(*position.get(), *scale.get()))

    def fillRectF(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl3.SDL_RenderFillRect(self._renderer, sdl3.SDL_FRect(*position.get(), *scale.get()))

    def createTextureFromSurface(self, surface) -> sdl3.SDL_POINTER[sdl3.SDL_Texture]:
        return sdl3.SDL_CreateTextureFromSurface(self._renderer, surface)
    
    def renderTexture(self, texture, position: Vector2, angle: float = 0.0, center: Vector2 = None) -> None:
        width, height = ctypes.c_float(0), ctypes.c_float(0)
        sdl3.SDL_GetTextureSize(texture, ctypes.byref(width), ctypes.byref(height))
        if center is None: center = Vector2(width.value / 2, height.value / 2)
        sdl3.SDL_RenderTextureRotated(self._renderer, texture, None, sdl3.SDL_FRect(*position.getInt(), width.value, height.value), angle, sdl3.SDL_FPoint(*center.getInt()), sdl3.SDL_FLIP_NONE)
    
    def renderSurface(self, surface, position: Vector2, angle: float = 0.0, center: Vector2 = None) -> None:
        texture = self.createTextureFromSurface(surface._surface.surface)
        self.renderTexture(texture, position, angle, center)
        sdl3.SDL_DestroyTexture(texture)

    def clear(self, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        sdl3.SDL_RenderClear(self._renderer)

    def present(self) -> None:
        sdl3.SDL_RenderPresent(self._renderer)

    def terminate(self) -> None:
        ...