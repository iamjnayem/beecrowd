salary = float(input())

def calculateTax(salary):
    
    if salary > 4500.00:
        tax = 999.99 * 0.08 + 1499.99 * 0.18 + (salary-4500)*0.28
        return tax 

    if salary > 3000.00 and salary <= 4500.00:
        tax = 999.99 * 0.08 + (salary-3000) * 0.18
        return tax 

    if salary > 2000.00 and salary <= 3000.00:
        tax = (salary-2000.00) * 0.08
        return tax 

if salary <= 2000:
    print("Isento")
else:
    print("R$ {0:0.2f}".format(calculateTax(salary)))
