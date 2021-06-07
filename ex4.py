my_str = input('Напишите несколько слов, используя пробелы: ')
my_str = my_str.split()
for i in range(len(my_str)):
    print(f'{i + 1}.', my_str[i][:11])
