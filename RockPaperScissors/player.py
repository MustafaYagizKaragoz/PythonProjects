import random


class Player:

    def __init__(self, name, is_human):
        self.__score = 0
        self.current_choice = ""
        self.__name = name
        self.__is_human = is_human
        self.__list = ["rock", "paper", "scissors"]

    def make_choise(self):
        if self.__is_human:
            self.current_choice = input(
                f"{self.__name}, make your choice rock,paper,scissors: "
            ).lower()
            while self.current_choice not in self.__list:
                print("Invalid choice please try again")
                self.current_choice = input(
                    f"{self.__name}, make your choice rock,paper,scissors: "
                ).lower()
        else:
            self.current_choice = random.choice(self.__list)
            print(f"{self.__name} chose {self.current_choice}")
        return self.current_choice

    def update_score(self):
        self.__score += 1

    def get_choice(self):
        return self.current_choice

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
