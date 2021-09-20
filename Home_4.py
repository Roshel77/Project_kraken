dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('h4_1.txt', 'w', encoding='utf-8') as fw, open ('h4.txt', 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
    for line in lines:
        s = line.split()
        s[0] = dict_num[s[0]]
        f_w = ' '.join(s), '\n'
        fw.writelines(f_w)