count = 0

for x in range(5):
    number = int(input())
    if number % 2 == 0:
        count += 1

print("{0} valores pares".format(count))