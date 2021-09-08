my_list = [7, 5, 3, 3, 2]
num = int(input('Введите число: '))

for el in range(len(my_list)):
    if my_list[el] == num:
        my_list.insert(el + 1, num)
        break
    elif my_list[0] < num:
            my_list.insert(0, num)
    elif my_list[-1] > num:
            my_list.append(num)
    elif my_list[el] > num and my_list[el + 1] < num:
            my_list.insert(el+1, num)
            break
print(my_list)