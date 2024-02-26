import reforge, sdl2, sdl2.ext, uuid

from reforge.math import Vector2, Vector4

class Component:
    def __init__(self) -> None:
        ...

    def onSetup(self):
        ...

    def onUpdate(self):
        ...

    def onExit(self):
        ...

class UUIDComponent(Component):
    def __init__(self, _uuid: uuid.UUID) -> None:
        super().__init__()
        self._uuid = _uuid

    def getUUID(self) -> uuid.UUID:
        return self._uuid

class NameComponent(Component):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def setName(self, name: str) -> None:
        self.name = name

class TransformComponent(Component):
    def __init__(self, position: Vector2, scale: Vector2, rotation: float) -> None:
        super().__init__()
        self.position, self.scale, self.rotation = position, scale, rotation

    def getPosition(self) -> Vector2:
        return self.position
    
    def setPosition(self, position: Vector2) -> None:
        self.position = position
    
    def getScale(self) -> Vector2:
        return self.scale

    def setScale(self, scale: Vector2) -> None:
        self.scale = scale
    
    def getRotation(self) -> float:
        return self.rotation

    def setRotation(self, rotation: float) -> None:
        self.rotation = rotation

class RectComponent(Component):
    def __init__(self, fill: bool, color: Vector4) -> None:
        super().__init__()
        self.fill, self.color = fill, color

    def getFill(self) -> bool:
        return self.fill

    def setFill(self, fill: bool) -> None:
        self.fill = fill
    
    def getColor(self) -> Vector4:
        return self.color

    def setColor(self, color: Vector4) -> None:
        self.color = color