first_day = int(input('Введите результат первого дня в км - '))
reach_result = int(input('Введите результат который хотите достигнуть в км - '))
result = 1
while first_day < reach_result:
    first_day = first_day + first_day * 0.1
    result += 1
print(f'на {result}-й день спортсмен достигнет результата - не менее {reach_result} км.')
