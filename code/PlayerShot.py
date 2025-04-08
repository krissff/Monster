#from code import Entity
from Const import ENTITY_SPEED
from code.entity import Entity

class PlayerShot(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]

    pass
