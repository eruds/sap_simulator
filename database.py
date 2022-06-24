from pet import *
from food import *
import random


class Database():
    @staticmethod
    def getRandomAnimal():
        animalsDB = [
            Duck(), Ant(), Beaver(), Cricket(), Fish(), Horse()
        ]
        return random.choice(animalsDB)
