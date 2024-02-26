import reforge, uuid

from reforge.entity import Entity

class Scene:
    def __init__(self):
        self.entities = {}

    def addEntity(self, entity: Entity, name: str = "Entity") -> None:
        _uuid = uuid.uuid4()
        while _uuid in self.entities: _uuid = uuid.uuid4()
        entity.addComponent(reforge.UUIDComponent(_uuid))
        entity.addComponent(reforge.NameComponent(name))
        entity.addComponent(reforge.TransformComponent(reforge.Vector2(0.0, 0.0), reforge.Vector2(100.0, 100.0), 0.0))
        self.entities[_uuid] = entity
        return _uuid
    
    def createEntity(self, name: str = "Entity") -> None:
        entity = Entity()
        self.addEntity(entity, name)
        return entity
    
    def removeEntity(self, _uuid: uuid.UUID) -> None:
        del self.entities[_uuid]
        return None

    def getEntities(self) -> reforge.List[Entity]:
        return list(self.entities.values())