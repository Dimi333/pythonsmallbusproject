import reactivex as rx
from Building import Building


class City:
    mainTimer = rx.interval(1)
    subs = {}
    buildings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, var):
        self.__name = var

    @property
    def gold(self):
        return self.__gold

    @gold.setter
    def gold(self, var):
        self.__gold = var

    @property
    def stone(self):
        return self.__stone

    @stone.setter
    def stone(self, var):
        self.__stone = var

    @property
    def wood(self):
        return self.__name

    @wood.setter
    def wood(self, var):
        self.__wood = var

    def __init__(self, name: str, gold: int, wood: int, stone: int):
        self.__name = name
        self.__gold = gold
        self.__wood = wood
        self.__stone = stone
        self.mainSub = self.mainTimer.subscribe(lambda value: self.checkAll())

    def printCity(self):
        print(f"Mesto {self.__name}\nZlato: {self.__gold} | Drevo: {self.__wood} | Kameň: {self.__stone}\n\nBudovy:")

        for b in self.buildings:
            print(self.buildings[b].name)

    def registerBuilding(self, building: Building):
        self.buildings[building.id] = building
        self.gold -= building.price
        self.subs[building.id] = self.mainTimer.subscribe(lambda value: building.build(1))

    def checkAll(self):
        for sub in self.subs:
            if self.buildings[sub].buildTime <= 0:
                self.subs[sub].dispose()

    def stopAll(self):
        self.mainSub.dispose()
        for sub in self.subs:
            self.subs[sub].dispose()
