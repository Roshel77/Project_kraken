class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

w1 = Position('Иван', 'Иванов', 'директор', 30000, 40000)
w2 = Position('Петр', 'Петров', 'дворник', 300000, 400000)
print(f'Полное имя: {w1.get_full_name()}. Должность: {w1.position}. Доход: {w1.get_total_income()}')
print(f'Полное имя: {w2.get_full_name()}. Должность: {w2.position}. Доход: {w2.get_total_income()}')