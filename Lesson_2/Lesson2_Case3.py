
my_cal = ['winter', 'spring', 'summer', 'autumn']
calendar = {
    1: 'зима',
    2: 'весна',
    3: 'лето',
    4: 'осень',
}
month = int(input('Введите месяц в числах от 1 до 12'))
if month in range(3,6):
    print(my_cal[1])
    print(calendar.get(2))
elif month in range(6,9):
    print(my_cal[2])
    print(calendar.get(3))
elif month in range(9, 12):
    print(my_cal[3])
    print(calendar.get(4))
elif month in range(1,3) or month == 12:
    print(my_cal[0])
    print(calendar.get(1))
else:
    print('Вы ввели неверное число')
