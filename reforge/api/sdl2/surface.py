import reforge.api.instanceHandler, sdl2, sdl2.ext

class Surface:
    def __init__(self, surface: sdl2.SDL_Surface) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.surface = surface

    def free(self) -> None:
        sdl2.SDL_FreeSurface(self.surface)
        self.surface = None

    def terminate(self) -> None:
        if self.surface is not None: self.free()