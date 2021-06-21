with open('text3.txt', 'r') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя величина дохода сотрудников = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Сотрудники у кого оклад менее 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')
