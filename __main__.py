""" Hlavný súbor """
from Mobile import Mobile
from Damage import Damage
from Battle import Battle
from City import City
from Building import Building
from uuid import uuid4
import os

if (os.name == "posix"):
    import console

gameRunning = True

player = Mobile(name="Player1", hp=100, AR=10, DR=8)
mob = Mobile(name="Mob1", hp=50, AR=5, DR=4)
damage = Damage(physical=1, magical=0, fire=0, cold=0, poison=0, electric=0, time=0)
city = City(name="Tomášov", gold=100, stone=50, wood=75)
battle = Battle(damage, player, mob)

while gameRunning:
    if os.name == 'posix':
        console.clear()
    else:
        os.system('cls')

    city.printCity()
    # battle.deal()
    
    print("1 - koniec, 2 - sklad, 3 - dom")

    menu = input()
    if menu == "2":
        building = Building(uuid4(), "Sklad", 10, 8)
        city.registerBuilding(building)
        
    if menu == "3":
        building = Building(uuid4(), "Dom", 5, 4)
        city.registerBuilding(building)

    if menu == "1":
        gameRunning = False
        city.stopAll()
