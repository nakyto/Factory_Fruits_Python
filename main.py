# creat by Théo le stagaire chez Tipee

from model import fruits
from model import apple
from model import lemon
from model import rasbery

def print_hi(name):
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    F1 = fruits.Fruit()
    F1.say()
    print("-------")
    F2 = apple.Apple()
    F2.say()
    print("-------")
    F3 = lemon.Lemon()
    F3.say()
    F3.testp()
    print("-------")
    F4 = rasbery.Rasbery()
    F4.say()
    print("-------")
