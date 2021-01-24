#1 вариант
def my_func(x, y):
    if y < 0:
        return abs(x) ** int(y)
    else:
        return abs(x) ** int(y * -1)


print(my_func(2, 4))

