testcase = int(input())

while testcase != 0:
    a, b = map(int, input().split())
    if a > b:
        temp = a 
        a = b
        b = temp
    sum = 0
    for i in range(a+1, b):
        if i % 2 == 1:
            sum += i 
    print(sum)
    testcase -= 1