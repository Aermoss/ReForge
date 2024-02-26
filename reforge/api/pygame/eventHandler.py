import reforge.api.tools, reforge.api.event, pygame, ctypes

class EventHandler:
    def __init__(self) -> None:
        reforge.api.tools.addInstance(__name__, self)
        self.eventQueue = []

    def pollEvents(self, eventRef: object) -> bool:
        try: events = pygame.event.get()
        except pygame.error: return False

        for event in events:
            if event.type == pygame.QUIT:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.WindowClosed, windowID = None))

            elif event.type == pygame.MOUSEMOTION:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseMotion, windowID = None, x = event.pos[0], y = event.pos[1]))

            elif event.type == pygame.MOUSEBUTTONUP:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseButtonUp, windowID = None, button = event.button))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseButtonDown, windowID = None, button = event.button))

            elif event.type == pygame.MOUSEWHEEL:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseWheel, x = event.x, y = event.y))

            else:
                ...

            del event

        if len(self.eventQueue) > 0:
            event = self.eventQueue.pop(0)

            for i in dir(event):
                if i.startswith("_"): continue
                setattr(eventRef, i, getattr(event, i))

            return True

    def terminate(self) -> None:
        ...