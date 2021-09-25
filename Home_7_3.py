class Cell:
    def __init__(self, num_cell):
        self.num_cell = int(num_cell)

    def __add__(self, other):
        return f'Объединение двух клеток: {self.num_cell + other.num_cell}'

    def __sub__(self, other):
        sub_cell = self.num_cell - other.num_cell
        if sub_cell > 0:
            return f'Уменьшенная клетка: {sub_cell}'
        else:
            return 'Клетки нет'

    def __mul__(self, other):
        return self.num_cell * other.num_cell

    def __truediv__(self, other):
        return self.num_cell // other.num_cell

    def make_order(self, line):
        res = ''
        sum_lines = self.num_cell / line
        for i in range(int(sum_lines)):
            res += '*' * line + '\n'
        res += '*' * (self.num_cell % line) + '\n'
        return res


cell_1 = Cell(31)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(6))