


# sub classe
from model.fruits import Fruit


class Apple(Fruit):

    def __init__(self):
        super().__init__()
        self.name = "Apple"

    def __str__(self):
        self.say()

    def say(self):
        print("I am a "+ self.name + " not the computer :)")
