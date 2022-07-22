from enum import Enum


class Espresso(Enum):
    water = 250
    milk = 0
    beans = 16
    cost = 4


class Latte(Enum):
    water = 350
    milk = 75
    beans = 20
    cost = 7


class Cappuccino(Enum):
    water = 200
    milk = 100
    beans = 12
    cost = 6

