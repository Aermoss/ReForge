import reforge.api.tools, reforge.api.event, sdl2, ctypes

class EventHandler:
    def __init__(self) -> None:
        reforge.api.tools.addInstance(__name__, self)
        self._event, self.eventQueue = sdl2.SDL_Event(), []

    def pollEvents(self, eventRef: object) -> bool:
        while sdl2.SDL_PollEvent(ctypes.byref(self._event)):
            if self._event.type == sdl2.SDL_WINDOWEVENT:
                if self._event.window.event == sdl2.SDL_WINDOWEVENT_CLOSE:
                    self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.WindowClosed, windowID = self._event.window.windowID))

            elif self._event.type == sdl2.SDL_MOUSEMOTION:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseMotion, windowID = self._event.motion.windowID, x = self._event.motion.x, y = self._event.motion.y))

            elif self._event.type == sdl2.SDL_MOUSEBUTTONUP:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseButtonUp, windowID = self._event.motion.windowID, button = self._event.button.button))

            elif self._event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseButtonDown, windowID = self._event.motion.windowID, button = self._event.button.button))

            elif self._event.type == sdl2.SDL_MOUSEWHEEL:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseWheel, x = self._event.wheel.x, y = self._event.wheel.y))

            else:
                ...

        if len(self.eventQueue) > 0:
            event = self.eventQueue.pop(0)

            for i in dir(event):
                if i.startswith("_"): continue
                setattr(eventRef, i, getattr(event, i))

            return True

    def terminate(self) -> None:
        ...