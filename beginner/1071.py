x = int(input())
y = int(input())

if x > y:
    temp = y
    y = x
    x = temp 


def sumOfOdd(x, y):
    sum = 0
    if x == y:
        print(0)
    else:
        for n in range(x+1, y):
            if n % 2 == 1:
                sum += n 
        print(sum)

sumOfOdd(x, y)



    




