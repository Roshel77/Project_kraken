class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем c помощью {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем c помощью {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем c помощью {self.title}')

s = Stationery('Канцелярия')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

s.draw()
pen.draw()
pencil.draw()
handle.draw()