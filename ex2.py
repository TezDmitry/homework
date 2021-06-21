with open('text2.txt', 'w', encoding='utf-8') as f:
    str_list = ['Hello World\n', 'I learn Python\n', 'Goodbye!\n']
    f.writelines(str_list)

with open('text2.txt', 'r', encoding='utf-8') as f:
    count_symbol = f.readlines()
    for i in range(len(count_symbol)):
        print(f'Количество символов {i + 1} строки - {len(count_symbol[i]) - 1}')
    f.seek(0)
    count_word = f.read()
    count_word = count_word.split()
    print(f'Общее количество слов - {len(count_word)}')
