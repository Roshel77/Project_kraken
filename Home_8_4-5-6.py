class Storage:
    def __init__(self):
        self.dict = {}

    def add_to(self, equip):
        self.dict.setdefault(equip.all_storage(), []).append(equip)

    def del_from(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop()


class Equipment:
    def __init__(self, sn, name, price, quantity):
        self.sn = sn
        self.name = name
        self.price = price
        self.quantity = quantity
        self.group = self.__class__.__name__

    def all_storage(self):
        return f'{self.group}'


class Printer(Equipment):
    def __init__(self, series, sn, name, price, quantity):
        super().__init__(name, sn, price, quantity)
        self.series = series

    def __repr__(self):
        return f'{self.name} серия: {self.series}; цена: {self.price}; кол-во: {self.quantity}'


class Scaner(Equipment):
    def __init__(self, speed, sn, name, price, quantity):
        super().__init__(name, sn, price, quantity)
        self.speed = speed

    def __repr__(self):
        return f'{self.name}; скорость: {self.speed}; цена: {self.price}; кол-во: {self.quantity}'


class Xerox(Equipment):
    def __init__(self, format, sn, name, price, quantity):
        super().__init__(name, sn, price, quantity)
        self.format = format

    def __repr__(self):
        return f'{self.name}; формат: {self.format}; цена:  {self.price}; кол-во: {self.quantity}'

storage = Storage()
scaner = Scaner('23', '3453574-6858', 'hp', '12300', 6)
storage.add_to(scaner)
scaner = Scaner('22', '3453654-6019', 'hp', '23490', 3)
storage.add_to(scaner)
xerox = Xerox('A4', '1298574-1012', 'Epson', '23900', 1)
storage.add_to(xerox)
printer = Printer('45-291', '4857293-1110', 'hp', 34920, 2)
storage.add_to(printer)
printer = Printer('30-291', '2039824-68', 'hp', 31920, 2)
storage.add_to(printer)
print(storage.dict)
storage.del_from('Printer')
print(storage.dict)