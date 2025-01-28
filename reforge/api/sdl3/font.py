import reforge.api.instanceHandler, reforge.api, sdl3

from reforge.math import Vector2, Vector3, Vector4

class Font:
    def __init__(self, filePath: str = None, size: int = 32) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.filePath, self.size, self.font = filePath, size, None
        self.load(filePath, size)

    def load(self, filePath: str, size: int) -> None:
        if self.font is not None: return self.free()
        self.filePath, self.size = filePath, size
        self.font = sdl3.TTF_OpenFont(self.filePath.encode(), self.size) \
            if self.filePath is not None else None
        
    def free(self) -> None:
        sdl3.TTF_CloseFont(self.font)
        self.font = None

    def render(self, text: str, color: Vector4) -> sdl3.SDL_Surface:
        if self.font is None: return reforge.getContextCurrent().logger.log(reforge.LogLevel.Error, "font is not loaded!")
        return reforge.api.Surface(sdl3.TTF_RenderText_Blended(self.font, text.encode(), 0, sdl3.SDL_Color(*[int(i) for i in color.get()])))

    def terminate(self) -> None:
        if self.font is not None: self.free()