with open('personel_salary.txt', encoding='utf-8') as s:
    salary = []
    min_salary = []
    personnel_salary = s.read().split('\n')
    print(personnel_salary)

    for i in personnel_salary:
        i = i.split()
        salary.append(i[1])
        if int(i[1]) < 20000:
            min_salary.append(i[0])
    mean_salary = sum(map(int, salary)) / len(salary)

print(f'Меньше 20000 руб получают {min_salary} \nСредний оклад {mean_salary}')