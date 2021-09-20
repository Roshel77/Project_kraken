with open('h3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    staff = []
    sum_zp = 0
    i = 0
    for line in lines:
        i += 1
        s = line.split()
        if float(s[1]) < 20000:
            staff.append(s[0])
        sum_zp += float(s[1])
        zp = sum_zp / i

    print(f'{staff} имеют зарплату меньше 20000р.')
    print(f'Размер средней заработной платы: {zp:.2f}')