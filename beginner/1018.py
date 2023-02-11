#banknotes

amount = int(input())

hundredNotes = amount // 100
rest = amount % 100

fiftyNotes = rest // 50;
rest = rest % 50


twentyNotes = rest // 20
rest = rest % 20

tenNotes = rest // 10
rest = rest % 10

fiveNotes = rest // 5
rest = rest % 5

twoNotes = rest // 2
rest = rest % 2

oneNotes = rest

print(amount)
print("{0} nota(s) de R$ 100,00".format(hundredNotes))
print("{0} nota(s) de R$ 50,00".format(fiftyNotes))
print("{0} nota(s) de R$ 20,00".format(twentyNotes))
print("{0} nota(s) de R$ 10,00".format(tenNotes))
print("{0} nota(s) de R$ 5,00".format(fiveNotes))
print("{0} nota(s) de R$ 2,00".format(twoNotes))
print("{0} nota(s) de R$ 1,00".format(oneNotes))








