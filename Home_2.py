with open('met.txt', 'r') as f:
    content = f.readlines()
    print(f'{len(content)} строки')
    for i in range(len(content)):
        words = content[i].split()
        print(f'В {i + 1} строке {len(words)} слов')