
from model import fruits
from model import apple
from model import lemon
from model import rasbery

class FruitFactory:

    def creat_fruts(self,name):
        if name == 'Apple' or name == 'apple':
            return apple.Apple()

        elif name == 'Lemon' or name == 'lemon':
            return lemon.Lemon()

        elif name == 'Rasbery' or name == 'rasbery':
            return rasbery.Rasbery()

