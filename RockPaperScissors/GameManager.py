class GameManager:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def is_finish(self):
        if self.player1.get_score() == 3:
            print(
                f"-------------------{self.player1.get_name()} won!!!!-----------------"
            )
            exit()
        elif self.player2.get_score() == 3:
            print(
                f"-------------------{self.player2.get_name()} won!!!!-----------------"
            )
            exit()

    def who_won(self):
        choice_1 = self.player1.get_choice()
        choice_2 = self.player2.get_choice()
        if choice_1 == choice_2:
            print("Draw")
        elif (choice_1 == "rock" and choice_2 == "scissors") or \
                (choice_1 == "paper" and choice_2 == "rock") or \
                (choice_1 == "scissors" and choice_2 == "paper"):
            self.player1.update_score()
            print(self.player1.get_name() + " won")
        else:
            self.player2.update_score()
            print(self.player2.get_name() + " won")
        print(f"{self.player1.get_name()} score: {self.player1.get_score()}")
        print(f"{self.player2.get_name()} score: {self.player2.get_score()}")
