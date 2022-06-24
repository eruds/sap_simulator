from enum import Enum, auto
# from colorama import Fore
from clint.textui import colored, puts

from player import Player
from pet import *


class BattleResult(Enum):
    WIN = auto()
    DRAW = auto()
    LOSE = auto()


class BattleStatus(Enum):
    STARTED = auto()
    ONGOING = auto()
    ENDED = auto()

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
    def pop(self): return self.stack.pop()


class Battler():
    def __init__(self):
        print("Battler Initiated")

    @staticmethod
    def battle(players: list[Player]):
        def getResult(player: BattleStack):
            return BattleResult.WIN if len(player) > 0 else BattleResult.LOSE
        # type (Player) -> None
        playerPets: list[BattleStack] = list(
            map(lambda player: BattleStack(player.pets), players))
        player1 = playerPets[0]
        player2 = playerPets[1]
        status = BattleStatus.STARTED

        # ? This is stupid
        pet1 = EmptyPet()
        pet2 = EmptyPet()
        # Cant end game if one of the player pet isnt dead yet
        while len(playerPets[0]) > 0 and len(playerPets[1]) > 0:
            print(player1)
            print(player2)
            # Take out the most front pet as the battler
            pet1 = player1.pop() if pet1.state == PetState.Faint or status == BattleStatus.STARTED else pet1
            pet2 = player2.pop() if pet2.state == PetState.Faint or status == BattleStatus.STARTED else pet2
            # Activate pet effects
            # Shows the Pet info before taking damage
            print(colored.green(f"Before {pet1} vs {pet2}"))
            # Battle Initiated
            pet1.takeDamage(pet2.attack)
            pet2.takeDamage(pet1.attack)
            # Shows the Pet info after taking damage
            print(colored.blue(f"After {pet1} vs {pet2}"))
            status = BattleStatus.ONGOING
        status = BattleStatus.ENDED
        return (getResult(player1), getResult(player2))
