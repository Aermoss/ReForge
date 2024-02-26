import reforge.api.tools, sdl2

class Context:
    def __init__(self) -> None:
        reforge.api.tools.addInstance(__name__, self)
        sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

    def terminate(self) -> None:
        sdl2.SDL_Quit()