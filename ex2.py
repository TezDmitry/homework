time = int(input('Введите время в секундах: '))
hours = time // 3600
minute = (time - hours * 3600) // 60
second = time - hours * 3600 - minute * 60
print(f'Время в формате чч:мм:сс - {hours:02d}:{minute:02d}:{second:02d}')
