# from colorama import Fore
import uuid
from clint.textui import colored, puts

from mechanics.states import *
from mechanics.player import Player
from mechanics.pet import Pet

# A Link Class to link two objects together


class Link():
    def __init__(self):
        print("Link Constructor")

# Pets is copied into the battle stack


class BattleStack():
    def __init__(self, pets: list[Pet]):
        self.stack: list[Pet] = []
        for pet in pets:
            if pet is not None:
                self.stack.append(pet)

    def __len__(self): return len(self.stack)
    # ? This looks stupid
    def __str__(self): return str(list(map(lambda pet: str(pet), self.stack)))
    def __getitem__(self, i): return self.stack[i]
    def pop(self): return self.stack.pop(0)


class BattleSystem():
    # * Only handles the player pets, not the player object itself
    # ! Turn this into a singleton
    #
    def __init__(self):
        self.__id = uuid.uuid4()
        self.__state = BattleState.STANDBY
        # Store the player pets. Turn the player pets into a battleStack.
        self.__playerPets = {}
        # Store the different events happening in a batlle. Reset before the next attack
        self.__events = []

    def addPlayer(self, player):
        playerPets = BattleStack(player.pets)
        for pet in playerPets:
            # Add the pet into the battle system
            # Open Access for the pet to send message to the BattleSystem
            pet.setInformant(self.__sendMessage)
        self.__playerPets[player.id] = playerPets

    def getPlayers(self):
        return list(self.__playerPets.values())

    # Broadcast system
    def clearEvents(self):
        self.__events = []

    def getState(self):
        return self.__state

    def changeState(self, state):
        if(state in BattleState):
            # ? Does this work
            self.__state = state
            # Notify other pets about the battle state change.
            self.__events.append(self.__state)
            self.__notify(self.__id)

    def __sendMessage(self, id: str, state: Trigger):
        # ? Do I need to check whether the function is being triggered by the pets
        # if(id not in self.__playerPets.)
        self.__events.append({id, state})
        # Notify other pets about the change
        self.__notify(id)

    def __notify(self, id):
        # Notify the pets on a change in battle phase state or pet change
        # TODO Need to check whether the pet is a friend or a foe
        # print(self.__playerPets)
        for pets in self.__playerPets.values():
            for pet in pets:
                if pet.id != id:
                    pet.update(self.__events)

    # Battle System
    # TODO fix this two functions
    def getResult(self, player: BattleStack):
        return BattleResult.WIN if len(player) > 0 else BattleResult.LOSE

    def checkLose(self, player: BattleStack):
        return len(player) == 0

# Right now its not inside any class
# A singular battle function


def battle(players: list[Player]):
    # * Handle player winning and losing score
    battleSystem = BattleSystem()
    # Add Players into the System
    for player in players:
        battleSystem.addPlayer(player)

    # type (Player) -> None

    # *The player1 and player2 items is connected to the object inside the battleSystem
    player1, player2 = battleSystem.getPlayers()
    print("Start of Battle")

    # Tracking the concurrent events in a battle
    # How to keep track the different pets that got damaged?
    # TODO check the battlesystem state change here
    event_list = []
    event_list.append(BattleState.BATTLESTART)

    while not battleSystem.checkLose(player1) and not battleSystem.checkLose(player2):
        # Define phases throughout the battle to determine
        pet1 = player1[0]
        pet2 = player2[0]
        print(player1)
        print(player2)

        # Activate pet effects
        # for pet in player1 :
        #     if pet.trigger() is in event_list :
        #         pet.activateEffect()

        # Start of Battle
        print(colored.green(f"Before : {pet1} vs {pet2}"))
        # Check pet effects

        # Damage accumulation
        pet1.takeDamage(pet2.attack)
        pet2.takeDamage(pet1.attack)
        # Check pet effects

        # End Of Battle
        print(colored.blue(f"After : {pet1} vs {pet2}"))

        # Check if pet Faints
        # Change this to an observer
        # Check pet effects
        if pet1.isFaint():
            player1.pop()
        if pet2.isFaint():
            player2.pop()

        # Clear the eventlists
        battleSystem.clearEvents()

    event_list.append(BattleState.BATTLEEND)
    return (battleSystem.getResult(player1), battleSystem.getResult(player2))
