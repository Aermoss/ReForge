import reforge.api.instanceHandler, reforge.api.event, sdl3, ctypes

class EventHandler:
    def __init__(self) -> None:
        reforge.api.instanceHandler.addInstance(__name__, self)
        self._event, self.eventQueue = sdl3.SDL_Event(), []

    def pollEvents(self, eventRef: object) -> bool:
        while sdl3.SDL_PollEvent(ctypes.byref(self._event)):
            if self._event.type == sdl3.SDL_EVENT_WINDOW_CLOSE_REQUESTED:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.WindowClosed, windowId = self._event.window.windowID))

            elif self._event.type == sdl3.SDL_EVENT_MOUSE_MOTION:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseMotion, windowId = self._event.motion.windowID, motion = reforge.Vector2(self._event.motion.x, self._event.motion.y)))

            elif self._event.type == sdl3.SDL_EVENT_MOUSE_BUTTON_UP:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseButtonUp, windowId = self._event.button.windowID, button = self._event.button.button))

            elif self._event.type == sdl3.SDL_EVENT_MOUSE_BUTTON_DOWN:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseButtonDown, windowId = self._event.button.windowID, button = self._event.button.button))

            elif self._event.type == sdl3.SDL_EVENT_MOUSE_WHEEL:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.MouseWheel, windowId = self._event.wheel.windowID, wheel = reforge.Vector2(self._event.wheel.x, self._event.wheel.y)))

            elif self._event.type == sdl3.SDL_EVENT_FINGER_MOTION:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.FingerMotion, windowId = self._event.tfinger.windowID, fingerId = self._event.tfinger.fingerId, motion = reforge.Vector2(self._event.tfinger.x, self._event.tfinger.y)))

            elif self._event.type == sdl3.SDL_EVENT_FINGER_UP:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.FingerUp, windowId = self._event.tfinger.windowID, fingerId = self._event.tfinger.fingerId))

            elif self._event.type == sdl3.SDL_EVENT_FINGER_DOWN:
                self.eventQueue.append(reforge.api.event.Event(type = reforge.api.event.EventType.FingerDown, windowId = self._event.tfinger.windowID, fingerId = self._event.tfinger.fingerId))

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