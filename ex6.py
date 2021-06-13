from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
print('*' * 50)

my_list = [1, 5, "Python", 'Hello']
counts = 0
for i in cycle(my_list):
    if counts > 9:
        break
    print(i)
    counts += 1
