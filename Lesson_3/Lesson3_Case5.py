def my_sum():
    sum_1 = 0
    while True:
        list_of_num = input('Введите числа')
        list_of_num.split()
        if list_of_num == 'q':
            print('Программа завершена')
            break
        for el in list(map(int, list_of_num)):
            sum_1 += el
        print(f'сумма чисел равна: {sum_1}')

        new_list_of_num = input("Введите еще числа или нажмите 'q' для выхода")
        list_of_num.split()
        if new_list_of_num == 'q':
            print('Программа завершена')
            break
        sum_2 = sum_1
        for el in list(map(int, new_list_of_num)):
            sum_2 += el
        print(f'Суммарный итог: {sum_2}')

print(my_sum())
