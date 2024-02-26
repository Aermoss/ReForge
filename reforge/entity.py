import reforge, sdl2, sdl2.ext, uuid

from reforge.components import Component

class Entity:
    def __init__(self) -> None:
        self.components, self.children, self.parent = {}, {}, None

    def onSetup(self) -> None:
        for component in self.components.values():
            component.onSetup()

        for child in self.children.values():
            child.onSetup()

    def onUpdate(self) -> None:
        for component in self.components.values():
            component.onUpdate()

        for child in self.children.values():
            child.onUpdate()

    def onExit(self) -> None:
        for component in self.components.values():
            component.onExit()

        for child in self.children.values():
            child.onExit()

    def addChild(self, entity: object) -> None:
        _uuid = uuid.uuid4()
        while _uuid in self.entities: _uuid = uuid.uuid4()
        self.children[_uuid] = entity
        entity.parent = self
        return _uuid
    
    def getChild(self, _uuid: uuid.UUID) -> object:
        return self.children[_uuid]
    
    def removeChild(self, _uuid: uuid.UUID) -> None:
        if self.children[_uuid].parent == self:
            self.children[_uuid].parent = None

        del self.children[_uuid]
        return None

    def addComponent(self, component: Component) -> None:
        if self.hasComponent(type(component)):
            reforge.getContextCurrent().logger.log(reforge.LogLevel.Error, "entity already has component of type " + component.__class__.__name__ + ".")
            return None
        
        self.components[component.__class__.__name__] = component
        return None

    def getComponent(self, componentType: type) -> Component:
        if componentType.__name__ in self.components:
            return self.components[componentType.__name__]

        else:
            reforge.getContextCurrent().logger.log(reforge.LogLevel.Error, "entity doesn't have component of type " + componentType.__name__ + ".")
            return None
    
    def hasComponent(self, componentType: type) -> bool:
        if componentType.__name__ in self.components: return True
        else: return False