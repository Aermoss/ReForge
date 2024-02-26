class EventType:
    Null, WindowClosed, MouseMotion, MouseButtonUp, MouseButtonDown, MouseWheel = range(6)

class Event:
    def __init__(self, type = EventType.Null, *args, **kwargs) -> None:
        self.type = type

        for i in kwargs:
            setattr(self, i, kwargs[i])