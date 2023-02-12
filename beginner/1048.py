salary = float(input())

def calculate(salary, percentage):
    return salary + (salary * percentage)/100
def formatMessage(salary, percentage):
    result = calculate(salary, percentage)
    print("Novo salario: {0:0.2f}".format(result))
    print("Reajuste ganho: {0:0.2f}".format(result - salary))
    print("Em percentual: {0} %".format(percentage))

if salary >= 0 and salary <= 400.00:
    formatMessage(salary, 15)
elif salary > 400.00 and salary <= 800.00:
    formatMessage(salary, 12)
elif salary > 800.00 and salary <= 1200.00:
    formatMessage(salary, 10)
elif salary > 1200.00 and salary <= 2000.00:
    formatMessage(salary, 7)
elif salary > 2000.00:
    formatMessage(salary, 4)
