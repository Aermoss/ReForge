import reforge.api.instanceHandler, sdl3

class Context:
    def __init__(self) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO | sdl3.SDL_INIT_AUDIO | sdl3.SDL_INIT_EVENTS)
        sdl3.TTF_Init()

    def terminate(self) -> None:
        sdl3.TTF_Quit()
        sdl3.SDL_Quit()