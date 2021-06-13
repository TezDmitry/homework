from sys import argv
try:
    print('Введите данные по порядку через пробел: Заработная плата сотрудника, ставка в час, премия')
    script_name, working_out_hours, rate_per_hour, prize = argv
    result = int(working_out_hours) * int(rate_per_hour) + int(prize)
    print(f'Заработная плата сотрудника, '
          f'выработка в часах({int(working_out_hours)}) * ставка в час({int(rate_per_hour)}) + премия({int(prize)}), '
          f'равна {result}')
except ValueError:
    print('Нужно ввести имя файла и три целых числовых значения')
