
from enum import Enum, auto
from clint.textui import colored, puts

from food import Food, FoodType


class PetState(Enum):
    Standby = auto()
    Buy = auto()
    Sell = auto()
    Summonned = auto()
    Faint = auto()
    Eat = auto()


class Pet():
    def __init__(self, id, name: str, attack: int, health: int):
        # print("Pet constructor")
        # id, Name, Level, Effect, State, Equipment, health, attack, damage
        self.id = id
        self.name: str = name
        self.level = 1
        # Adjust this according to the shop battle etc
        self.state = PetState.Standby
        self.health = health
        self.attack = attack
    # Info

    def __str__(self) -> str:
        # return f"Name : {self.name}, Level : {self.level}, Attack : {self.attack}, health : {self.health}"
        return f"{self.name} | {self.level} | {self.attack} | {self.health}"

    def info(self):
        # print(f"Name : {self.name}, health : {self.health}, attack : {self.attack}")
        print(f"{self.name} | {self.attack} | {self.health}")
    # Setter and Getters

    def takeDamage(self, damage: int):
        print(colored.red(f"{self} took {damage} damage"))
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.state = PetState.Faint

    # Mechanics
    def activateEffect(self):
        print("Effect activated")

    def eatFood(self, food: Food):
        if(Food.type == FoodType.Instant):
            self.attack += food.attack
            self.health += food.health
        else:
            self.Equipment = food

# Hotfix


class EmptyPet(Pet):
    def __init__(self):
        super(EmptyPet, self).__init__(0, "Empty", 0, 0)


class Duck(Pet):
    def __init__(self):
        super(Duck, self).__init__(1, "Duck", 2, 3)


class Ant(Pet):
    def __init__(self):
        super(Ant, self).__init__(2, "Ant", 2, 1)


class Beaver(Pet):
    def __init__(self):
        super(Beaver, self).__init__(3, "Beaver", 3, 2)


class Cricket(Pet):
    def __init__(self):
        super(Cricket, self).__init__(4, "Cricket", 1, 2)


class Fish(Pet):
    def __init__(self):
        super(Fish, self).__init__(5, "Fish", 2, 2)


class Horse(Pet):
    def __init__(self):
        super(Horse, self).__init__(6, "Horse", 2, 1)
