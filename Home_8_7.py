class ComplexNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма x1 и x2: x = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение x1 и x2: x = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'x = {self.a} + {self.b} * i'

x1 = ComplexNum(1, -2)
x2 = ComplexNum(3, 4)
print(x1 + x2)
print(x1 * x2)