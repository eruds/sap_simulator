# from colorama import Fore
from clint.textui import colored, puts

from states import *
from player import Player
from pet import *

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


class Battler():
    def __init__(self):
        print("Battler Initiated")

    @staticmethod
    def battle(players: list[Player]):
        def getResult(player: BattleStack):
            return BattleResult.WIN if len(player) > 0 else BattleResult.LOSE

        def checkLose(player: BattleStack):
            return len(player) == 0
        # type (Player) -> None
        playerPets: list[BattleStack] = list(
            map(lambda player: BattleStack(player.pets), players))
        player1 = playerPets[0]
        player2 = playerPets[1]
        print("Start of Battle")

        # Tracking the concurrent events in a battle
        # How to keep track the different pets that got damaged?
        event_list = []
        event_list.append(BattleState.BATTLESTART)

        while not checkLose(player1) and not checkLose(player2):
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
            # Check pet effects
            if pet1.isFaint():
                player1.pop()
            if pet2.isFaint():
                player2.pop()

            # Clear the eventlists
            event_list = []

        event_list.append(BattleState.BATTLEEND)
        return (getResult(player1), getResult(player2))
