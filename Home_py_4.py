str = input('Введите текст через пробел: ').split(' ')
my_list = list(str)
for i in range(len(my_list)):
    my_list1 = my_list[i]
    print(i+1, my_list1[:10])