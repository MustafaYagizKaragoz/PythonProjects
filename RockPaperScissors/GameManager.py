class GameManager:
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
        self.is_finish=False

    def is_finish(self):
        if self.player1.score==3:
            self.is_finish=True
            exit()
        elif self.player2.score==3:
            self.is_finish=True
            exit()
    def who_won(self,choice_1,choice_2):
        #todo: check  who won
        pass
