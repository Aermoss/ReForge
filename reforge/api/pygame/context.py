import reforge.api.instanceHandler, pygame

class Context:
    def __init__(self) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        pygame.init()

    def terminate(self) -> None:
        pygame.quit()