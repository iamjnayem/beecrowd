code1, unit1, unit_price1 = input().split(' ')
code2, unit2, unit_price2 = input().split(' ')

code1 = int(code1)
code2 = int(code2)

unit1 = int(unit1)
unit2 = int(unit2)

unit_price1 = float(unit_price1)
unit_price2 = float(unit_price2)


print("VALOR A PAGAR: R$ {0:0.2f}".format(unit1 * unit_price1 + unit2 * unit_price2))



