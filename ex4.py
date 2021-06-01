number = int(input('Введите целое положительное число - '))
num_max = 0
while number > 0:
    numb = number % 10
    if numb > num_max:
        num_max = numb
    number = number // 10
print(num_max)
