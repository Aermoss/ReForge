import reforge.api.instanceHandler, pygame

class Window:
    def __init__(self, title: str, width: int, height: int) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.title, self.width, self.height, self.flags = title, width, height, 0
        pygame.display.set_mode((width, height), self.flags, vsync = False)
        pygame.display.set_caption(title)

    def terminate(self) -> None:
        pygame.display.quit()