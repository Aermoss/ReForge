import reforge.api.instanceHandler, pygame

from reforge.math import Vector2, Vector3, Vector4

class Font:
    def __init__(self, filePath: str = None, size: int = 32) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.filePath, self.size, self.font = filePath, size, None
        self.load(filePath, size)

    def load(self, filePath: str, size: int) -> None:
        if self.font is not None: return self.free()
        self.filePath, self.size = filePath, size
        self.font = pygame.font.Font(self.filePath, self.size) \
            if self.filePath is not None else None
        
    def free(self) -> None:
        self.font = None

    def render(self, text: str, color: Vector4) -> pygame.Surface:
        if self.font is None: return reforge.getContextCurrent().logger.log(reforge.LogLevel.Error, "font is not loaded!")
        return reforge.api.Surface(self.font.render(text, True, color.get()[:3]))

    def terminate(self) -> None:
        if self.font is not None: self.free()