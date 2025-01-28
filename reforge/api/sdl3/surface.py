import reforge.api.instanceHandler, sdl3

class Surface:
    def __init__(self, surface: sdl3.SDL_Surface) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.surface = surface

    def free(self) -> None:
        sdl3.SDL_DestroySurface(self.surface)
        self.surface = None

    def terminate(self) -> None:
        if self.surface is not None: self.free()