# Задача 1
a = 7
b = 9
c = a / b
print(c)

date = input('Введите год рождения')
place = input('Введите меcто рождения')
print(date)
print(place)

#Задача 2
date = int(input('Введите время в секундах'))
min = date // 60
hour = min // 60
sec = hour - min
print(f'Время: {hour}: {min}: {sec}')

#Задача 3
num = int(input('Введите любое целое число'))
print(int(num) + int(num + num) + int(num + num + num))

#Задача 4 - без понятия

#Задача 5
revenues = int(input('Сумма выручки'))
expencese = int(input('Сумма издержек'))
result = revenues - expencese
if result <= 0:
    print('Компания работает в убыток')
else:
    print(f'Прибыль компании составляет {result:.2f} рублей')
    profit = result/revenues
    print(f'Рентабельность выручки составляет: {profit:.2f} рублей')
    pers = int(input('Введите число сотрудников'))
    profit_per_pers = result/pers
    print(f'Прибыль компании в расчете на 1 сотрудника составляет:{profit_per_pers:.2f} рублей')

#Задача 6
a = int(input('Введите стартовое расстояние'))
b = int(input('Введите желаемое расстояние'))
day = 1
print(f'1-й день пробежки: {a:.2f}')
while a <= b:
    a = a * 0.1 + a
    day += 1
    print(f'{day}-й день пробежки: {a:.2f}')
else:
    print(f"На {day}-й день спортсмен достиг результата - не менее 3 км")
