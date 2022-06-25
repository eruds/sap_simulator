from pet import *
from food import *
from states import *
import random
import json


class Database():
    @staticmethod
    def getRandomAnimal():
        # animalsDB = json.load(open("18.0_pets.json"))
        # Only tier ones for pack 1 for testing
        animalsDB = json.load(open("tierOnePets.json"))

        # Filter Tier One
        # animalsDB = list(
        #     filter(lambda pet: pet["Tier"] is 1 and "Pack1" in pet["Packs"], animalsDB))

        # Only Faints
        # print(animalsDB)
        animalsDB = list(filter(
            lambda pet: pet["Abilities"][0]["Trigger"] == "Faint",
            animalsDB
        ))

        # for pet in animalsDB:
        # print(pet["Abilities"][0]["Trigger"] == "Faint")

        randAnimal = random.choice(animalsDB)
        # print(randAnimal)
        return Pet(
            randAnimal["Id"],
            randAnimal["Name"],
            randAnimal["Attack"],
            randAnimal["Health"],
            randAnimal["Tier"],
            randAnimal["Packs"],
            Trigger.getTrigger(randAnimal["Abilities"][0]["Trigger"])
        )
