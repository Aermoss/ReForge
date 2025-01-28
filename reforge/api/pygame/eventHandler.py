import reforge.api.instanceHandler, reforge.api.event, pygame, ctypes

class EventHandler:
    def __init__(self) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self.eventQueue = []

    def pollEvents(self, eventRef: object) -> bool:
        try: events = pygame.event.get()
        except pygame.error: return False

        for event in events:
            if event.type == pygame.QUIT:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.WindowClosed, windowId = None))

            elif event.type == pygame.MOUSEMOTION:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseMotion, windowId = None, motion = reforge.Vector2(*event.pos)))

            elif event.type == pygame.MOUSEBUTTONUP:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseButtonUp, windowId = None, button = event.button))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseButtonDown, windowId = None, button = event.button))

            elif event.type == pygame.MOUSEWHEEL:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseWheel, windowId = None, wheel = reforge.Vector2(event.x, event.y)))

            elif event.type == pygame.FINGERMOTION:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.FingerMotion, windowId = None, fingerId = event.finger_id, motion = reforge.Vector2(event.x, event.y)))

            elif event.type == pygame.FINGERUP:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.FingerUp, windowId = None, fingerId = event.finger_id))

            elif event.type == pygame.FINGERDOWN:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.FingerDown, windowId = None, fingerId = event.finger_id))

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