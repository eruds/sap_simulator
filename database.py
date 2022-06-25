from pet import *
from food import *
import random
import json


class Database():
    @staticmethod
    def getRandomAnimal():
        animalsDB = json.load(open("18.0_pets.json"))

        # Filter Tier One
        animalsDB = list(
            filter(lambda pet: pet["Tier"] is 1 and "Pack1" in pet["Packs"], animalsDB))

        randAnimal = random.choice(animalsDB)
        # print(randAnimal)
        return Pet(
            randAnimal["Id"],
            randAnimal["Name"],
            randAnimal["Attack"],
            randAnimal["Health"],
            randAnimal["Tier"],
            randAnimal["Packs"],
            Trigger.TURNSTART
        )
