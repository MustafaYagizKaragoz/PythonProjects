from dice import Dice
from player import Player


class Game:

    def __init__(self, players, dice):
        self.players = players
        self.dice = dice

    def play_round(self):

        for player in self.players:
            roll = player.roll_dice(self.dice)
            print(f"{player.name} {roll}")

    def determine_winner(self):            
        scores = {player.name: sum(player.rolls) for player in self.players}
        winner = max(scores, key=scores.get)
        return winner, scores[winner]


if __name__ == '__main__':
    dice=Dice()
    p1 = Player("Ecem")
    p2 = Player("Mustafa")
    game = Game([p1, p2], dice)

    for i in range(5):
       game.play_round()
    winner, score = game.determine_winner()
    print(f"\n The winner is {winner} ")
