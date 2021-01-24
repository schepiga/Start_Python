
data = {}

with open('text6.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()

    for i in my_list:
        result = i.replace('(', ' ').split()
        data = {result[0][0:-1]: sum(int(i) for i in result if i.isdigit())}
        print(data)

