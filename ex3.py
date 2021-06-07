# Решение с помощью dict and list
month = int(input('Введите номер месяца ввиде числа: '))
month_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
if month in month_dict.get('зима'):
    print('Зима')
elif month in month_dict.get('весна'):
    print('Весна')
elif month in month_dict.get('лето'):
    print('Лето')
elif month in month_dict.get('осень'):
    print('Осень')
else:
    print('Ошибка ввода')

# Решение с помощью list
month = int(input('Введите номер месяца ввиде числа: '))
month_list = ['Зима', 'Весна', 'Лето', 'Осень']
number_month = [i for i in range(1, 13)]
result = None
for el in number_month:
    if el == month:
        el = month
        break
if month > 12 or month < 1:
    print('В году всего 12 месяцев, введите корректное число заново')
elif 3 <= month <= 5:
    result = month_list[1]
elif 6 <= month <= 8:
    result = month_list[2]
elif 9 <= month <= 11:
    result = month_list[3]
else:
    result = month_list[0]
print(result)
