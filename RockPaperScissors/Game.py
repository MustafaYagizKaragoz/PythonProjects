from player import Player
from GameManager import GameManager


class Game:
    def create_player(self,player1_name,player1_is_human,player2_name,player2_is_human):
        self.player1=Player(player1_name,player1_is_human)
        self.player2=Player(player2_name,player2_is_human)
        self.gm=GameManager(self.player1,self.player2)

    def play_game(self):
        while True:
            choice_1=self.player1.make_choise()
            choice_2=self.player2.make_choise()
            self.gm.who_won()
            self.gm.is_finish()

if __name__=="__main__":
    game=Game()
    game.create_player("Ecem",True,"Pc",True)
    game.play_game()