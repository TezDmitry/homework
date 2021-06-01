proceeds = int(input('Введите значение выручки у фирмы - '))
costs = int(input('Введите значение издержек фирмы - '))
if proceeds > costs:
    print('Фирма работает в прибыль')
    profit = proceeds - costs
    print(f'Рентабельности фирмы равна {profit / proceeds}')
    person = int(input('Введите численность работников фирмы - '))
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {profit / person}')
elif proceeds < costs:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в нуль')
