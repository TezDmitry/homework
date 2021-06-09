def my_sum_numbers():
    total = 0
    output = True
    while output == True:
        numbers = input('Введите числа или нажмите спец. символ(Q) для выхода - ').split()
        result = 0
        for i in range(len(numbers)):
            if numbers[i] == 'Q' or numbers[i] == 'q':
                output = False
                break
            else:
                result = result + int(numbers[i])
        total = total + result
        print(f'Суммы всех числе равна {total}')


my_sum_numbers()

