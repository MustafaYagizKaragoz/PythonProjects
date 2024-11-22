import random


class GameManager:

    def __init__(self):
        self.guessed_letter = []
        self.word_list = ["apple", "banana", "watermelon"]
        self.choosen_word = random.choice(self.word_list)
        self.correct_letter = []
        self.tries = 6

    def guess(self, guess):
        guess = guess.lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabetic character.")
            return
        if guess in self.guessed_letter:
            print("You have written this letter before!\n")
        elif guess == ' ':
            print("You cant enter a space")
        elif guess in self.choosen_word:
            print(f"Correct! {guess} is in word  list\n")
            self.correct_letter.append(guess)
        else:
            self.tries -= 1
            if self.tries != 0:
                print(
                    f"Wrong! {guess} is not in word {self.tries} chances left\n"
                )
        self.show()
        if self.is_finish():
            exit()
        self.guessed_letter.append(guess)

    def get_len(self):
        return len(self.choosen_word)

    def show(self):
        word = self.choosen_word
        for i in word:
            if i in self.correct_letter:
                print(i, end=" ")
            else:
                print('_', end=" ")

    def is_finish(self):
        if all(letter in self.correct_letter for letter in self.choosen_word):
            print("\nCongratulations! You guessed the word!")
            return True

        # Kaybetme durumu
        if self.tries <= 0:
            print(f"\nGame Over! The word was: {self.choosen_word}")
            return True

        return False