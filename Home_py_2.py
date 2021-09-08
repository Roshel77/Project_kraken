my_str = input("Введите перечень элементов списка: ")
str = list(my_str)
for i in range(0, len(str)-1, 2):
    str[i], str[i+1] = str[i+1], str[i]
print(str)