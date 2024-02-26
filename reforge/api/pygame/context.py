import reforge.api.tools, pygame

class Context:
    def __init__(self) -> None:
        reforge.api.tools.addInstance(__name__, self)
        pygame.init()

    def terminate(self) -> None:
        pygame.quit()