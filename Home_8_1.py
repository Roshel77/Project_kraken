class Data:
    def __init__(self, data_1):
       self.data_1 = str(data_1)


    @classmethod
    def date(cls, data_1):
        my_date = []
        for i in data_1.split():
            if i != '-':
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])


    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and year == 2021:
            return f'Верная дата'
        else:
            return f'Неправильная дата'

print(Data.date('14 - 10 - 2021'))
print(Data.valid(14, 10, 2021))