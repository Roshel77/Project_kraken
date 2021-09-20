sub_dict = {}
with open('h6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        key = line.split()[0]
        value = line.split()[1:]
        v = sum(map(int, value))
        sub_dict[key] = v
    print(sub_dict)