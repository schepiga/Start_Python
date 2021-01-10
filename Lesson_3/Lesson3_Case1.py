def division_numbers():
    try:
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число больше нуля: "))
        result = num_1 / num_2
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    else:
        print(f'Частное от деления чисел: {result}')

division_numbers()

