def my_func(num_1, num_2, num_3):
    min_num = min(num_1, num_2, num_3)
    if num_1 == min_num:
        return num_2 + num_3
    elif num_2 == min_num:
        return num_1 + num_3
    else:
        return num_2 + num_1

print(f'Сумма двух наибольших чисел равна {my_func(int(input("Введите первое число ")), int(input("Введите второе число ")), int(input("Введите третье число ")))}')
