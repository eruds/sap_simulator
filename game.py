from enum import Enum, auto 

from player import Player
from battler import Battler 
from pet import *
from database import Database

class GameStatus(Enum) :
    Initiated = auto()
    Playing = auto()
    Ended = auto()


class Game():
    def __init__(self) :
        print("Game Initiated")
        self.status = GameStatus.Initiated
        self.players = [Player(1), Player(2)]
    # def test(self) :
    #     self.something = "Things"
    def test(self) :
        for player in self.players :
            for i in range(3) :
                player.addPet(Database.getRandomAnimal(), i)
    def play(self) :
        self.test()
        # print(self.something)
        self.status = GameStatus.Playing
        result = Battler.battle(self.players)
        print(result)
        if(result[0] == result[1]) : 
            print("Its a Draw!")
        else : 
            print(f"Player 1 {result[0]}")
            print(f"Player 2 {result[1]}")
Game().play()