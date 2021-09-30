class Division_Zero:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def func(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return f'На ноль делить нельзя'

div = Division_Zero(100, 2)
print(div.func(100, 2))
print(div.func(100, 0))
