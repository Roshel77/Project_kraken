with open('h5.txt', 'w') as fw:
    line = input('Введите числа через пробел: ')
    fw.writelines(line)
    num = line.split()
    sum_num = sum(map(int, num))
    print(sum_num)