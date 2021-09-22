class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt(self):
        self.weight = 25
        self.height = 5
        print(f'Масса асфальта: {self._length * self._width * self.weight * self.height / 1000}')

r = Road(20, 5000)
r.mass_asphalt()