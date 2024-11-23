import random
class Player:
    def __init__(self,name,is_human):
        self.score=0
        self.current_choice=""
        self.__name=""
        self.__is_human=True
        self.__list=["rock","paper","scissors"]
    def make_choise(self):
        if self.__is_human:
            self.current_choice=input(f"{self.__name}, make your choice rock,paper,scissors: ").lower()
            while self.current_choice not in self.__list:
                print("Invalid choice please try again")
                self.current_choice=input(f"{self.__name}, make your choice rock,paper,scissors: ").lower()
        else:
            self.current_choice=random.choice(self.__list)
        return self.current_choice
    def  update_score(self):
        self.score+=1
    def reset_score(self):
        self.score=0
    def get_choice(self):
        return self.current_choice
