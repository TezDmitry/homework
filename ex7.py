from itertools import count
from math import factorial


def fact():
    for numb in count(1):
        yield factorial(numb)


try:
    gen = fact()
    counts = 0
    number = int(input('Введите до кого числа считать факториал - '))
    for i in gen:
        if counts < number:
            print(i)
            counts += 1
        else:
            break
except ValueError:
    print('Нужно ввести целое положительное число')
