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
        for i in scene.getEntities():
            if i.hasComponent(reforge.RectComponent):
                rect = i.getComponent(reforge.RectComponent)
                transform = i.getComponent(reforge.TransformComponent)
                {True: self._renderer.fillRectF, False: self._renderer.drawRectF}[rect.fill] \
                    (transform.position.x, transform.position.y, transform.scale.x, transform.scale.y, rect.color)

    def terminate(self) -> None:
        self._renderer.terminate()
        self._renderer = None