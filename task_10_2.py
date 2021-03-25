from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f'{res}'


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.size/6.5 + 0.5)


class Costume(Clothes):
    @property
    def consumption(self):
        return round((2*self.size + 0.3)/100)


coat1 = Coat(48)
coat2 = Coat(44)
costume1 = Costume(176)
print(coat1 + costume1 + coat2)
