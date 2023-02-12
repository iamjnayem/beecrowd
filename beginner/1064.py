numbers = []

for x in range(6):
    num = input()
    numbers.append(float(num))

count = 0
sum = 0

for x in numbers:
    if x > 0:
        count += 1
        sum += x 
    
print("{0} valores positivos".format(count))
print("{0:0.1f}".format(sum/count))