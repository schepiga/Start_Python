
my_list = []
n = 4
for i in range(n):
    i = input('Введите элементы списка')
    my_list.append(i)
if n % 2 == 0:
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
else:
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    last_el = my_list[-1]
    my_list.append(last_el)
print(my_list)

