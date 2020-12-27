my_list = [7, 5, 3, 3, 2]
ratio = int(input('Оцените от 1 до 10'))
ratio_max = (max(my_list))
if ratio_max <= ratio < 10 and ratio > 0:
    my_list.insert(0, ratio)
    print(my_list)
elif ratio not in my_list and 10 > ratio > 0:
    my_list.append(ratio)
    print(my_list)
elif ratio in my_list and 10 > ratio > 0:
    same_ratio = my_list.index(ratio)
    my_list.insert(same_ratio, ratio)
    print(my_list)
else:
    print('Вы ввели неверное число')

