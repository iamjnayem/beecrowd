start = int(input())
def printOdd(start):
    for x in range(6):
        print(start)
        start += 2

if start % 2 == 1:
    printOdd(start)
else:
    start = start + 1
    printOdd(start)