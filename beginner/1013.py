def biggerNumber(a, b):
    return (a + b + abs(a - b))//2


a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

biggest = biggerNumber(biggerNumber(a, b), c)
print("{0} eh o maior".format(biggest))