from card import Card
import random
class Game:
    def __init__(self,symbols) -> None:
        self.cards = [Card(symbol) for symbol in symbols for _ in range(2)]
        random.shuffle(self.cards)
        self.score = 0
        self.tries=0
    def update_score(self):
        self.score+=1
    def update_tries(self):
        self.tries+=1
    def display_board(self):
        for index, card in enumerate(self.cards):
            print(f"{index + 1}: {card}", end="  ")
            if (index + 1) % 4 == 0:
                print()  # 4 kartta bir satır atla
        print()
    def play_turn(self,first_choice,second_choice):
        first_card=self.cards[first_choice-1]
        second_card=self.cards[second_choice-1]
        
        first_card.reveal()
        second_card.reveal()
        self.display_board()
        
        if first_card.symbol == second_card.symbol:
            print("Target matched! 👏 \n --------------------------------------------------")
            self.update_score()
        
        else:
            print("Target unmatched Cards are hiding \n --------------------------------------------------")
            first_card.hide()
            second_card.hide()
        self.update_tries()
    def is_over(self):
        return all(card.is_open for card in self.cards)
    
    
    def start(self):
        print("Welcome to the Memory Game! 🎮") 
        while not self.is_over():
            self.display_board()
            try:
                first_choice=int(input("Enter first card number: "))
                second_choice=int(input("Enter second card number: "))
                
                if first_choice == second_choice:
                    print("You can not select the same card. Please try again")
                    continue
                if not (1 <= first_choice <= len(self.cards)) or not (1 <= second_choice <= len(self.cards)):
                    print("Enter a valid card number")
                    continue
                        
                if self.cards[first_choice-1].is_open or self.cards[second_choice-1].is_open:
                    print("You already selected those cards")
                    continue
                self.play_turn(first_choice,second_choice)
            except ValueError:
                print("Please just enter integer number !")
            finally:
                print(f"Congrulations you won the game {self.score}")
                print(f"Your tries "+self.tries())     
if __name__ == "__main__":
    symbols = ["🍎", "🍌", "🍇", "🍓", "🍒", "🍍", "🍉", "🥝"]
    game=Game(symbols)
    game.start()