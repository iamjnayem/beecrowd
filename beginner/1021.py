amount = input()
notes = int(amount.split('.')[0])
paisa = int(amount.split('.')[1])

hundredNotes = notes // 100
rest = notes % 100

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

fiftyPaisa = paisa // 50;
rest = paisa % 50;

twentyFivePaisa = rest // 25;
rest = rest % 25;

tenPaisa = rest // 10;
rest = rest % 10;

fivePaisa = rest // 5;
rest = rest % 5;

onePaisa = rest;


print("NOTAS:")
print("{0} nota(s) de R$ 100.00".format(hundredNotes))
print("{0} nota(s) de R$ 50.00".format(fiftyNotes))
print("{0} nota(s) de R$ 20.00".format(twentyNotes))
print("{0} nota(s) de R$ 10.00".format(tenNotes))
print("{0} nota(s) de R$ 5.00".format(fiveNotes))
print("{0} nota(s) de R$ 2.00".format(twoNotes))

print("MOEDAS:")
print("{0} moeda(s) de R$ 1.00".format(oneNotes))
print("{0} moeda(s) de R$ 0.50".format(fiftyPaisa))
print("{0} moeda(s) de R$ 0.25".format(twentyFivePaisa))
print("{0} moeda(s) de R$ 0.10".format(tenPaisa))
print("{0} moeda(s) de R$ 0.05".format(fivePaisa))
print("{0} moeda(s) de R$ 0.01".format(onePaisa))

