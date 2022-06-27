Database for the game. Explanation of the keywords will be explained here

>

    "Level": Level of the pet
    "Trigger": What triggers the effect. Faint, Sell, Buy, LevelUp, Hurt, **Add More**
    "Type": Response to the trigger.    >>
        Give : Give stat points,
        Gain : Gain stat points,
        Deal : Deal damage to another pet
        Summon : Summon another animal
    *Extention to Type*
    "Summon": What animal is being summoned
    >>
        Fixed : Zombie Cricket, Bee, Etc
        Pack  : What animal from what pack
    "GiveType": The kind stat giving
    >>
        Perm : Permanent Stat Gain
        Temp : Temporary ( Until End of Battle ) Stat Gain
    "Target":
    >>
        Random : A Random Target
        Fixed : A Fixed Target
        All : All pet on the area
    "TargetType": "Friend",
    >>
        Friend : A pet used by the same player
        Enemy : A pet used by the opponent player
    "TargetCount": How Many Target. Integer number,
    "Stats": Deal/Gain/Give ammount (Attack/Health) or (Damage/0) for Deal. Also the stat for what being summoned
