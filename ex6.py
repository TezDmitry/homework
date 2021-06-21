my_dict = {}
with open('text6.txt', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        elems = [i for i in stats if i == ' ' or ('0' <= i <= '9')]
        name_sum = sum(map(int, ''.join(elems).split()))
        my_dict[name] = name_sum
print(f'{my_dict}')
