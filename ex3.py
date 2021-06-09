def my_func(num1, num2, num3):
    """ Функция находит минимально значение
        из num1, num2, num3 и, сравнивает
        его с одним из значений.
        Если они равны, то функция возвращает
        значение суммы двух других значений
    """
    if min(num1, num2, num3) == num1:
        return num2 + num3
    elif min(num1, num2, num3) == num2:
        return num1 + num3
    return num2 + num1


print(my_func(25, 50, 25))
