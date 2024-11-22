from hanging import GameManager
gm = GameManager()
print("\nWelcome to Hangman!")
gm.show()

while gm.tries > 0:  
    guess = input("\n\nEnter your guess: ").strip()
    if not guess:
        print("Please enter a valid letter.")
        continue

    gm.guess(guess)
