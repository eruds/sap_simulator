from pet import *

class Player() :
    def __init__(self, id) :
        maxPet : int = 5
        # id, Health, Wins, Gold Owned, Turn, Pets Owned
        print("Player constructor")
        self.id = id
        self.pets = [None for x in range(maxPet)]
    # Get Player Choice
    # Available choices : 
    # Buy Shop
    # Roll Shop
    # Move Pet 
    # Start Battle
    # def choose(self) :

    # Setters 
    # Status 
    def removeHealth(self, damage) :
        self.health -= damage
    def addWin(self) :
        self.addWin += 1
    # Pets
    def addPet(self, pet : Pet, index : int) :
        if(index < 0 or index >= len(self.pets) ) :
            raise "Index out of bounds"
        self.pets[index] = pet
    
    # Getters
    def getPetCount(self) :
        return len(filter(lambda pet: pet.status == PetState.standby, self.pets))
