import reforge.api.instanceHandler, sdl2, sdl2.ext, sdl2.sdlttf

class Context:
    def __init__(self) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
        sdl2.sdlttf.TTF_Init()

    def terminate(self) -> None:
        sdl2.SDL_Quit()