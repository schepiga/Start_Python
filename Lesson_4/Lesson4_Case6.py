from itertools import count, cycle

for x in count(3):
    if x > 10:
        break
    else:
        print(x, end='')


c = 0
for y in cycle('Ля'):
    if c > 12:
        break
    else:
        c += 1
        print(y, end='')




