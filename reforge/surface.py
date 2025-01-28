import reforge.api

class Surface:
    def __init__(self, surface: reforge.api.Surface) -> None:
        self._surface = surface

    def free(self) -> None:
        self._surface.free()

    def terminate(self) -> None:
        self._surface.terminate()