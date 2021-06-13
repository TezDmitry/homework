numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
number = [numbers[i + 1] for i in range(len(numbers) - 1) if numbers[i + 1] > numbers[i]]
print(number)
