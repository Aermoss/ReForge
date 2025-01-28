import reforge

from reforge.components import Component

class Entity:
    def __init__(self, scene: object = None, name: str = None) -> None:
        self.scene, self.components = scene, {}

        if scene is not None:
            scene.registerEntity(self, name)
            self.onCreate()

    def addComponent(self, component: Component) -> None:
        if self.hasComponent(component):
            reforge.getContextCurrent().logger.log(reforge.LogLevel.Error, "component already exists.")
            return

        self.addOrReplaceComponent(component)

    def addOrReplaceComponent(self, component: Component) -> None:
        self.components[component.__class__.__name__] = component
        component.entity = self

    def hasComponent(self, component: Component) -> bool:
        return (component.__class__.__name__ if component.__class__ != type else component.__name__) in self.components

    def getComponent(self, component: Component) -> Component:
        if not self.hasComponent(component):
            reforge.getContextCurrent().logger.log(reforge.LogLevel.Error, "component doesn't exist.")
            return
        
        return self.components[component.__name__]
    
    def removeComponent(self, component: Component) -> None:
        if not self.hasComponent(component):
            reforge.getContextCurrent().logger.log(reforge.LogLevel.Error, "component doesn't exist.")
            return
        
        del self.components[component.__name__]

    def onCreate(self) -> None:
        for i in self.components:
            self.components[i].onCreate()

    def onUpdate(self, deltaTime: float) -> None:
        for i in self.components:
            self.components[i].onUpdate(deltaTime)

    def onDestroy(self) -> None:
        for i in self.components:
            self.components[i].onDestroy()