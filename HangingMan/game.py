from hanging import GameManager

gm = GameManager()

gm.show()
while gm.tries > -1:
    if gm.tries == 0:
        print("\nYou lose!")
        break
    guess = str(input("\nEnter your guess: "))
    gm.guess(guess)
