import json

with open("firm_income_file.json", "w", encoding='utf-8') as jason_f:
    with open('text7.txt', 'r', encoding='utf-8') as f:
        for i in f:
            profit_dict = {i.split()[0]: int(i.split()[2]) - int(i.split()[3])}
            #print(profit_dict.values())
            for x in profit_dict.values():
                if x > 0:
                    mean_profit = {'средняя прибыль': sum(map(int, profit_dict.values())) / len(profit_dict.values())}
        #print(mean_profit)

    data = [mean_profit, profit_dict]

    json.dump(data, jason_f)

