from abc import ABC, abstractmethod


class Clothes:

    def __init__(self, param):
        self.param = param

    @property
    def total_text(self):
        return f'Общий расход ткани: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def some_print(self):
        pass


class Coat(Clothes):

    def total_textile(self):
        return f'Расход ткани на пальто: {self.param / 6.5 + 0.5 :.2f}'

    def some_print(self):
        print('Пальто')


class Costume(Clothes):
    def total_textile(self):
        return f'Расход ткани на костюм: {2 * self.param + 0.3 :.2f}'

    def some_print(self):
        print('Костюм')


coat = Coat(400)
costume = Costume(55)
print(coat.total_textile())
print(costume.total_textile())
coat.some_print()
costume.some_print()
print(costume.total_text)