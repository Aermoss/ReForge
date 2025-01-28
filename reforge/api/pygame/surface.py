import reforge.api.instanceHandler, pygame

class Surface:
    def __init__(self, surface: pygame.Surface) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.surface = surface

    def free(self) -> None:
        self.surface = None

    def terminate(self) -> None:
        if self.surface is not None: self.free()