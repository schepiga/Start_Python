a = [1, 2, 5, 1, 4, 7, 2, 3]

list_a = [i for i in range(len(a)) if a.count(i) == 1]

print(a)
print(list_a)

