russian_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text4m.txt', 'w', encoding='utf-8') as mf:
    with open('text4.txt', 'r') as f:
        mf.write(str([line.replace(line.split()[0], russian_dict.get(line.split()[0])) for line in f]))
