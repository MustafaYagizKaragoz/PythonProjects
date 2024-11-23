class Player:
    def __init__(self,name):
        self.score=0
        self.current_choice=""
        self.name=""
    def make_choise(self):
        #TODO the player will choose betwenn,rock,paper,scissors
        pass
    def  update_score(self):
        self.score+=1
    def reset_score(self):
        self.score=0
    def get_choice(self):
        return self.current_choice


