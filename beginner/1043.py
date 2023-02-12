a, b, c = map(float, input().split(' '))

if a + b > c and b + c > a and c + a > b:
    print("Perimetro = {0:0.1f}".format(a + b + c))
else:
    print("Area = {0:0.1f}".format(0.5 * (a + b) * c))