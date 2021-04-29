
# ABSTRACT Classe

class Fruit:
    # private
    # name = ""

    def __init__(self):
        self.name = "fruit"

    def __str__(self):
        self.say()

    def say(self):
        print("i am a " + self.name)

