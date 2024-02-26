import reforge.api.tools, reforge.api.event, pygame, inspect

from reforge.math import Vector4

class Renderer:
    def __init__(self, window, vsync = False) -> None:
        reforge.api.tools.addInstance(__name__, self)
        self.window, self.vsync = window, vsync
        self._surface = pygame.display.set_mode((self.window.width, self.window.height), self.window.flags, vsync = self.vsync)
        self.drawColor = Vector4(0, 0, 0, 255)

    def setDrawColor(self, color: Vector4) -> None:
        self.drawColor = color

    def setViewport(self, x: int, y: int, width: int, height: int) -> None:
        ...

    def setVSync(self, vsync: bool) -> None:
        self.vsync = vsync
        try: self._surface = pygame.display.set_mode((self.window.width, self.window.height), self.window.flags, vsync = self.vsync)
        except pygame.error: ...

    def setScale(self, x: float, y: float) -> None:
        ...

    def drawRect(self, x: int, y: int, width: int, height: int, color: Vector4 = None) -> None:
        self.drawRectF(int(x), int(y), int(width), int(height), color)

    def drawRectF(self, x: float, y: float, width: float, height: float, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        try: pygame.draw.rect(self._surface, self.drawColor.get()[:3], pygame.Rect(x, y, width, height), width = 1)
        except pygame.error: ...

    def fillRect(self, x: int, y: int, width: int, height: int, color: Vector4 = None) -> None:
        self.fillRectF(int(x), int(y), int(width), int(height), color)

    def fillRectF(self, x: float, y: float, width: float, height: float, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        try: pygame.draw.rect(self._surface, self.drawColor.get()[:3], pygame.Rect(x, y, width, height), width = 0)
        except pygame.error: ...

    def clear(self, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        try: self._surface.fill(self.drawColor.get()[:3])
        except pygame.error: ...

    def present(self) -> None:
        try: pygame.display.flip()
        except pygame.error: ...

    def terminate(self) -> None:
        ...