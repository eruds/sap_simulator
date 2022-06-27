from mechanics.player import Player
from mechanics.battler import BattleSystem, battle
from mechanics.pet import *
from data.database import Database

from mechanics.states import *


class Game():
    # ! Turn this into a singleton
    # *Can handle more than 2 players
    def __init__(self):
        print("Game Initiated")
        self.status = GameState.Initiated
        self.players = [Player(), Player()]

    def test(self):
        # Used to test the system. Currently testing the battler
        # Give players random starting animals
        for player in self.players:
            for i in range(3):
                player.addPet(Database.getRandomAnimal(), i)

    # ! Add function to display player info

    def playerTurn(self):
        # Try multithreading
        print("Player doing their turn")

    def play(self):
        self.test()
        self.status = GameState.Playing
        # Run Every Player turns
        # When every player is finished, match every player for a one on one battle
        # Add every two player into a battle

        result = battle(self.players)
        print(result)
        if(result[0] == result[1]):
            print("Its a Draw!")
        else:
            print(f"Player 1 {result[0]}")
            print(f"Player 2 {result[1]}")
