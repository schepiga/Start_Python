from functools import reduce
list_of_num = [x for x in range(100, 1001) if x % 2 == 0]

def multiply(a, b):
    return a * b

print(list_of_num)
print(reduce(multiply, list_of_num))