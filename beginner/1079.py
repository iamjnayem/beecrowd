n = int(input())

for i in range(n):
    myList = list(map(float, input().split(" ")))
    sum = myList[0] * 2 + myList[1] * 3 + myList[2] * 5
    avg = sum / (2 + 3 + 5)
    print("{0:0.1f}".format(avg))



