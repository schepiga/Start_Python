def factorial(n):
    fac_num = 1
    for n in range(1, n+1):
        fac_num *= n
        yield fac_num

for el in factorial(5):
    print(el)





