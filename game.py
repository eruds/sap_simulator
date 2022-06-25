from player import Player
from battler import Battler 
from pet import *
from database import Database

from states import * 



class Game():
    def __init__(self) :
        print("Game Initiated")
        self.status = GameState.Initiated
        self.players = [Player(1), Player(2)]
    def test(self) :
        # Used to test the system. Currently testing the battler
        # Give players random starting animals 
        for player in self.players :
            for i in range(3) :
                player.addPet(Database.getRandomAnimal(), i)
    def playerTurn(self) :
        # Try multithreading 
        print("Player doing their turn")
    def play(self) :
        self.test()
        self.status = GameState.Playing
        result = Battler.battle(self.players)
        print(result)
        if(result[0] == result[1]) : 
            print("Its a Draw!")
        else : 
            print(f"Player 1 {result[0]}")
            print(f"Player 2 {result[1]}")
Game().play()