def my_func(x, y):
    """ Функция возводит число х в степень y
        И возвращает результат
    """
    return x ** y


print(my_func(2, -6))


my_func = lambda x, y: x ** y
print(my_func(2, -5))


def my_func(x, y):
    """
        Функция возводит число х в степень y,
        используя цикл for, производя уммножение
        х на х в количестве модуля y
    """
    result = 1
    for _ in range(abs(y)):
        result *= x
    return print(1 / result)


my_func(2, -6)
