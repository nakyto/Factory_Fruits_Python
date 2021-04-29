
# sub classe
from model.fruits import Fruit

# sub classe

class Rasbery(Fruit):

    def __init__(self):
        super().__init__()
        self.name = "Rasbery"

    def __str__(self):
        self.say()

    def say(self):
        print("I am a " + self.name + "you see my friends, * RasberyPI * ")
