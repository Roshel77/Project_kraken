class Only_num:
    def __init__(self, *args):
        self.my_list = []

    def list1(self):
        while True:
            try:
                i = int(input('Введите число: '))
                self.my_list.append(i)
                print(f'Текущий список: {self.my_list}')
            except:
                print(f'Вы ввели не число, введите stop для выхода или введите число: ')
                stop = input()
                if stop == 'stop':
                    return f'Ввод завершен, итоговый список: {self.my_list}'
                else:
                    print(self.list1())

nums = Only_num(0)
print(nums.list1())