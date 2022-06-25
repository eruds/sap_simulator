from enum import Enum, auto 

class GameState(Enum) :
    Initiated = auto()
    Playing = auto()
    Ended = auto()

class TurnState(Enum) :
    TURNSTART = auto()
    TURNEND = auto()

class BattleResult(Enum):
    WIN = auto()
    DRAW = auto()
    LOSE = auto()

class BattleState(Enum):
    BATTLESTART = auto()
    BATTLEEND = auto()


class PetState(Enum):
    Standby = auto()
    Buy = auto()
    Sell = auto()
    Eat = auto()
    Summonned = auto()
    Hurt = auto()
    Attack = auto()
    Faint = auto()

# Hotfix
class Trigger(Enum):
    Standby = auto()
    Buy = auto()
    Sell = auto()
    Eat = auto()
    Summonned = auto()
    Hurt = auto()
    Attack = auto()
    Faint = auto()
    BATTLESTART = auto()
    BATTLEEND = auto()
    TURNSTART = auto()
    TURNEND = auto()
     