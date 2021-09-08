month = input('Введите порядковый номер месяца - ')
enter = int(month)
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [12, 1, 2]
spring = [3, 4, 5]
if enter in summer:
    print('Это лето!')
elif enter in autumn:
    print('Это осень!')
elif enter in winter:
    print('Это зима!')
else:
    print('Это весна')



month = int(input('Введите порядковый номер месяца - '))
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
for key in seasons.keys():
    if month in seasons[key]:
        print(key)