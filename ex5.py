from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, [num for num in range(100, 1001, 2)]))
