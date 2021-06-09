def get_div(num1, num2):
    """ Функция определяет результат деления
        num1 на num2, и возвращает его.
        Обрабатывает ситуацию, когда
        происходит деление на нуль.
    """
    while True:
        if num2 != 0:
            return print(f'{num1} / {num2} = {(num1 / num2):.3f}')
        else:
            print('Деление на нуль нельзя')
            num1, num2 = int(input('Введите число: ')), int(input('Введите число: '))
            continue


get_div(int(input('Введите число: ')), int(input('Введите число: ')))


# while True:
#     num1 = int(input('Введите число: '))
#     num2 = int(input('Введите число: '))
#     if num2 == 0:
#         print('Деление на нуль нельзя')
#         continue
#     else:
#         print((lambda num1, num2: round(num1 / num2))(num1, num2))
#         break

