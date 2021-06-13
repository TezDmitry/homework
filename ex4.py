numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
number = [numbers[number] for number in range(len(numbers)) if numbers.count(numbers[number]) == 1]
print(number)
