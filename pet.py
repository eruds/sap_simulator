import uuid
from clint.textui import colored, puts

from food import Food, FoodType
from states import *


class Pet():
    def __init__(self,
                 petid: int,
                 name: str,
                 attack: int,
                 health: int,
                 tier: int,
                 packs: list[str],
                 trigger: Trigger):
        # print("Pet constructor")
        # id, Name, Level, Effect, State, Equipment, health, attack, damage
        self.id = uuid.uuid4()
        self.petid = petid
        self.name: str = name
        self.level = 1
        # Adjust this according to the shop battle etc
        self.state = PetState.Standby
        self.health = health
        self.attack = attack
        # Mechanics
        self.trigger = trigger
        # Set trigger based on petid
        # self.__setTrigger()
    # Info

    def __setTrigger(self):
        if self.petid == 0:
            self.trigger = Trigger.Faint
        if self.petid == 1:
            self.trigger = Trigger.Sell

    def __str__(self) -> str:
        # return f"Name : {self.name}, Level : {self.level}, Attack : {self.attack}, health : {self.health}"
        return f"{self.name} | {self.level} | {self.attack} | {self.health}"

    def info(self):
        # print(f"Name : {self.name}, health : {self.health}, attack : {self.attack}")
        print(f"{self.name} | {self.attack} | {self.health}")

    def isFaint(self):
        return self.state == PetState.Faint
    # Setter and Getters

    def takeDamage(self, damage: int):
        print(colored.red(f"{self} took {damage} damage"))
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.state = PetState.Faint
            print(colored.red(f"{self} fainted!"))

    # Mechanics
    def getBuff(self, attack, health):
        self.attack += attack
        self.health += health

    def eatFood(self, food: Food):
        if(Food.type == FoodType.Instant):
            self.attack += food.attack
            self.health += food.health
        else:
            self.Equipment = food

    def checkTrigger(self, externalTrigger=None):
        if(not externalTrigger):
            print(self.state == self.trigger)
        else:
            print(externalTrigger == self.trigger)
        print("Trigger Checked")

    def activateEffect(self):
        print("Effect activated")

# Hotfix
# class Duck(Pet):
#     def __init__(self):
#         super(Duck, self).__init__(1, "Duck", 2, 3)


# class Ant(Pet):
#     def __init__(self):
#         super(Ant, self).__init__(2, "Ant", 2, 1)


# class Beaver(Pet):
#     def __init__(self):
#         super(Beaver, self).__init__(3, "Beaver", 3, 2)


# class Cricket(Pet):
#     def __init__(self):
#         super(Cricket, self).__init__(4, "Cricket", 1, 2)


# class Fish(Pet):
#     def __init__(self):
#         super(Fish, self).__init__(5, "Fish", 2, 2)


# class Horse(Pet):
#     def __init__(self):
#         super(Horse, self).__init__(6, "Horse", 2, 1)
