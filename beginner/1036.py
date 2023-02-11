import math

a, b, c = [float(x) for x in input().split(' ')]

if (b**2 - 4 * a * c) < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(b** 2 - 4 * a * c))/(2 * a)
    x2 = (-b - math.sqrt(b** 2 - 4 * a * c))/(2 * a)

    print("R1 = {0:0.5f}".format(x1))
    print("R2 = {0:0.5f}".format(x2))
