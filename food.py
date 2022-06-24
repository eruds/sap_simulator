from enum import Enum, auto

class FoodType(Enum) :
    Instant = auto()
    Equipment = auto()

# Food Structure 
# If Instant :
# Attack and Health Buff
# If Equipment:
# Details on each individual food

class Food() :
    def __init__(self) :
        print("Food constructor")
        