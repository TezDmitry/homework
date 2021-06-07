my_list = list(input('Напишите что-то - '))
number = 0
for _ in range(len(my_list) // 2):
    my_list[number], my_list[number + 1] = my_list[number + 1], my_list[number]
    number += 2
print(my_list)
