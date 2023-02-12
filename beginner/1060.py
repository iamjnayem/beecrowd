numbers = []

for x in range(6):
    num = float(input())
    numbers.append(num)

count = 0
for item in numbers:
    if item > 0:
        count += 1
print("{0} valores positivos".format(count))