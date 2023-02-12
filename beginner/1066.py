even = 0
odd = 0
positive = 0
negative = 0

for x in range(5):
    number = int(input())
    if number % 2 == 0:
        even += 1
    if number % 2 == 1:
        odd += 1
    if number > 0:
        positive += 1
    if number < 0:
        negative += 1

print("{0} valor(es) par(es)".format(even))
print("{0} valor(es) impar(es)".format(odd))
print("{0} valor(es) positivo(s)".format(positive))
print("{0} valor(es) negativo(s)".format(negative))