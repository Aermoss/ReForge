import reforge, uuid

from reforge.entity import Entity

class Scene:
    def __init__(self) -> None:
        self.entities = {}

    def getEntities(self) -> reforge.List[Entity]:
        return list(self.entities.values())

    def registerEntity(self, entity: Entity, name: str = None, parent: Entity = None) -> None:
        entity.addComponent(reforge.IdComponent(id = uuid.uuid4()))
        entity.addComponent(reforge.NameComponent(name = name))
        entity.addComponent(reforge.TransformComponent(translation = reforge.Vector2(0.0, 0.0), scale = reforge.Vector2(1.0, 1.0)))
        entity.addComponent(reforge.RelationshipComponent(parent = parent))
        self.entities[entity.getComponent(reforge.IdComponent).id] = entity

    def removeEntity(self, entity: Entity) -> None:
        del self.entities[entity.getComponent(reforge.IdComponent).id]

    def createEntity(self, name: str = None, parent: Entity = None) -> None:
        entity = Entity()
        self.registerEntity(entity, name, parent)
        entity.onCreate()
        return entity

    def destroyEntity(self, entity: Entity) -> None:
        entity.onDestroy()
        self.removeEntity(entity)

    def update(self, deltaTime: float) -> None:
        for id in self.entities.copy():
            self.entities[id].onUpdate(deltaTime)

    def destroy(self) -> None:
        for id in self.entities.copy():
            self.destroyEntity(self.entities[id])