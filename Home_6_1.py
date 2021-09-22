import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    print('Светофор включился:')

    def running(self):
        print(f'{TrafficLight.__color[0]} свет')
        time.sleep(7)
        print(f'{TrafficLight.__color[1]} свет')
        time.sleep(2)
        print(f'{TrafficLight.__color[2]} свет')
        time.sleep(3)


t = TrafficLight()
print(t.running())