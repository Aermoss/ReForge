import reforge.api, pygame

from reforge.math import Vector2, Vector3, Vector4

class Renderer:
    def __init__(self, window, vsync = False) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.window, self.vsync = window, vsync
        self._surface = pygame.display.set_mode((self.window.width, self.window.height), self.window.flags, vsync = self.vsync)
        self.drawColor = Vector4(0.0, 0.0, 0.0, 255.0)

    def setDrawColor(self, color: Vector4) -> None:
        self.drawColor = color

    def setViewport(self, x: int, y: int, width: int, height: int) -> None:
        ...

    def setVSync(self, vsync: bool) -> None:
        self.vsync = vsync
        self._surface = pygame.display.set_mode((self.window.width, self.window.height), self.window.flags, vsync = self.vsync)

    def setScale(self, x: float, y: float) -> None:
        ...

    def drawRect(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        self.drawRectF(*position.getInt(), *scale.getInt(), color)

    def drawRectF(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        pygame.draw.rect(self._surface, self.drawColor.get()[:3], pygame.Rect(*position.get(), *scale.get()), width = 1)

    def fillRect(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        self.fillRectF(*position.getInt(), *scale.getInt(), color)

    def fillRectF(self, position: Vector2, scale: Vector2, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        pygame.draw.rect(self._surface, self.drawColor.get()[:3], pygame.Rect(*position.get(), *scale.get()), width = 0)

    def renderSurface(self, surface, position: Vector2, angle: float = 0.0) -> None:
        _surface = pygame.transform.rotate(surface._surface.surface, -angle)
        self._surface.blit(_surface, _surface.get_rect(center = _surface.get_rect(topleft = position.get()).center))

    def clear(self, color: Vector4 = None) -> None:
        if color != None: self.setDrawColor(color)
        self._surface.fill(self.drawColor.get()[:3])

    def present(self) -> None:
        pygame.display.flip()

    def terminate(self) -> None:
        ...