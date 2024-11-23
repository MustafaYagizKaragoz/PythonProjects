from player import Player
from GameManager import GameManager

p1=Player('Mustafa',is_human=True)
p2=Player("PC",is_human=False)
gm=GameManager(p1,p2)

playable=True
while playable:
    choice_1=p1.make_choise()
    choice_2=p2.make_choise()
    gm.who_won()
    gm.is_finish()

