from uuid import uuid4


class Building:
    id: uuid4
    wholeName: str
    name: str
    buildTime: int
    price: int
    health: int

    def __init__(self, id: uuid4, name: str, buildTime: int, price: int):
        self.id = id
        self.wholeName = name
        self.name = name
        self.buildTime = buildTime
        self.health = 0
        self.price = price

    def build(self, amount: int):
        self.health += int(amount)
        self.buildTime -= int(amount)
        self.name = self.wholeName + " " + str(self.buildTime)

    def Print(self):
        print(self.name)
