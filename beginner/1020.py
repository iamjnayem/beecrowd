days = int(input())

years = days // 365
rest = days % 365

months = rest // 30
rest = rest % 30

days = rest


print("{0} ano(s)".format(years))
print("{0} mes(es)".format(months))
print("{0} dia(s)".format(days))

