with open('text1.txt', 'w', encoding='utf-8') as f:
    while True:
        my_line = input('Введите что-то - ')
        if not my_line:
            break
        f.write(f'{my_line}\n')
