import reforge, uuid

from reforge.math import Vector2, Vector3, Vector4
from reforge.font import Font

class Component:
    def onCreate(self) -> None: ...
    def onUpdate(self, deltaTime) -> None: ...
    def onDestroy(self) -> None: ...

class IdComponent(Component):
    def __init__(self, id: uuid.uuid4) -> None:
        self.id = id

class NameComponent(Component):
    def __init__(self, name: str) -> None:
        self.name = name

class TransformComponent(Component):
    def __init__(self, translation: reforge.Vector2, scale: reforge.Vector2) -> None:
        self.__translation, self.__scale = translation, scale

    def translate(self, translation: reforge.Vector2) -> None:
        self.__translation += translation

    def setTranslation(self, translation: reforge.Vector2) -> None:
        self.__translation = translation

    def getTranslation(self) -> reforge.Vector2:
        return self.__translation
    
    def getWorldTranslation(self) -> reforge.Vector2:
        if self.entity.getComponent(RelationshipComponent).getParent() is None: return self.__translation
        else: return self.__translation + self.entity.getComponent(RelationshipComponent).getParent().getComponent(TransformComponent).getWorldTranslation()
    
    def scale(self, scale: reforge.Vector2) -> None:
        self.__scale *= scale

    def setScale(self, scale: reforge.Vector2) -> None:
        self.__scale = scale

    def getScale(self) -> reforge.Vector2:
        return self.__scale
    
    def getWorldScale(self) -> reforge.Vector2:
        if self.entity.getComponent(RelationshipComponent).getParent() is None: return self.__scale
        else: return self.__scale * self.entity.getComponent(RelationshipComponent).getParent().getComponent(TransformComponent).getWorldScale()

class RelationshipComponent(Component):
    def __init__(self, parent: object = None, children: reforge.Dict[uuid.uuid4, object] = {}) -> None:
        self.parent, self.children = parent, children

    def setParent(self, parent: object) -> None:
        if self.parent != None:
            self.parent.getComponent(RelationshipComponent).removeChild(self.entity, check = False)

        self.parent = parent

        if self.parent != None:
            self.parent.getComponent(RelationshipComponent).addChild(self.entity, check = False)

    def getParent(self):
        return self.parent

    def addChild(self, child: object, check: bool = True) -> bool:
        self.children[child.getComponent(IdComponent).id] = child

        if child.getComponent(RelationshipComponent).parent != self.entity and check:
            child.getComponent(RelationshipComponent).setParent(self.entity)

    def removeChild(self, child: object, check: bool = True) -> bool:
        if child.getComponent(RelationshipComponent).parent == self.entity and check:
            child.getComponent(RelationshipComponent).setParent(None)

        self.children.pop(child.getComponent(IdComponent).id)

class RectComponent(Component):
    def __init__(self, color: reforge.Vector4, fill: bool = True, borderWidth: int = 0, borderRadius = 0):
        self.color, self.fill, self.borderWidth, self.borderRadius = color, fill, borderWidth, borderRadius

class TextComponent(Component):
    def __init__(self, text: str, font: Font, color: reforge.Vector4):
        self.text, self.font, self.color = text, font, color

    @property
    def surface(self) -> reforge.Surface:
        return self.font.render(self.text, self.color)