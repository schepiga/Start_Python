from sys import argv

script_name, worker_hour, rate_per_hour, bonus = argv

def pers_salary():
    salary = int(worker_hour) * int(rate_per_hour) + int(bonus)
    print(salary)
    return

pers_salary()









