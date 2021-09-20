with open('data.txt', 'w') as f:
    while True:
        content = input('Введите текст: ')
        if content == '':
            break
        f.write(content + '\n')