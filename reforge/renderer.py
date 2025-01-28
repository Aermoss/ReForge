import reforge

from reforge.window import Window
from reforge.math import Vector4
from reforge.scene import Scene

class Renderer:
    def __init__(self, window: Window) -> None:
        self.window = window
        self._renderer = reforge.api.Renderer(window._window)

    def clear(self, color: Vector4 = None) -> None:
        self._renderer.clear(color)

    def present(self) -> None:
        self._renderer.present()

    def renderScene(self, scene: Scene):
        for entity in scene.getEntities():
            transform = entity.getComponent(reforge.TransformComponent)

            if entity.hasComponent(reforge.RectComponent):
                (self._renderer.fillRectF if entity.getComponent(reforge.RectComponent).fill else self._renderer.drawRectF) \
                    (transform.getWorldTranslation(), transform.getWorldScale(), entity.getComponent(reforge.RectComponent).color)
                
            if entity.hasComponent(reforge.TextComponent):
                text = entity.getComponent(reforge.TextComponent)
                self._renderer.renderSurface(text.surface, transform.getWorldTranslation())

    def terminate(self) -> None:
        self._renderer.terminate()
        self._renderer = None