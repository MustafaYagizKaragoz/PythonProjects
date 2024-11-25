class Player:

    def __init__(self, name):
        self.name = name
        self.rolls = []

    def roll_dice(self, dice):
        result = dice.roll()
        self.rolls.append(result)
        return result
