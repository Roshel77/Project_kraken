class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return f'{self.name} поехала'

    def turn(self):
        return f'повернула направо'

    def show_speed(self):
        return f'её текущая скорость: {self.speed}'

    def stop(self):
        return f'и остановилась'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили разрешенную в городе скорость!'
        else:
            return f'её текущая скорость: {self.speed}'


class SportCar(Car):
    def sport(self):
        return f'Поздравляю у тебя спортивная машина!'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость!'
        else:
            return f'её текущая скорость: {self.speed}'


class PoliceCar(Car):
    def police(self):
        return f'Это полицейская машина'

honda = Car(200, 'Черная', 'Accord')
print(f'{honda.color} {honda.go()}, {honda.show_speed()}, {honda.turn()} {honda.stop()}')
ford = TownCar(70, 'Белая', 'Фокус')
print(f'{ford.color} {ford.go()}, {ford.show_speed()}, {ford.turn()} {ford.stop()}')
porsche = SportCar(300, 'Желтая', 'Carrera')
print(f'{porsche.sport()} {porsche.color} {porsche.go()}, {porsche.show_speed()}, {porsche.turn()} {porsche.stop()}')
kia = WorkCar(70, 'Красная', 'Соренто')
print(f'{kia.color} {kia.go()}, {kia.show_speed()}, {kia.turn()} {kia.stop()}')
lada = PoliceCar(20, 'Черная', 'Калина')
print(f'{lada.police()} {lada.color} {lada.go()}, {lada.show_speed()}, {lada.turn()} {lada.stop()}')