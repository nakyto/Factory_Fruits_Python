
# sub classe
from model.fruits import Fruit

# sub classe

class Lemon(Fruit):

    def __init__(self):
        super().__init__()
        self.name = "Lemon"
        self.test = str(self.__class__.__name__)

    def __str__(self):
        self.say()


    def say(self):
        print("I am a " + self.name + " warning i pik ")

    def testp(self):
        print(self.test)
