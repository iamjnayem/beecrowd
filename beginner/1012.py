a,b,c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)

triangle = 0.5 * a * c
circle = 3.14159 * c * c 
trapezium = 0.5 * (a + b) * c; 
square = b * b;
rect = a * b;

print("TRIANGULO: {0:0.3f}".format(triangle))
print("CIRCULO: {0:0.3f}".format(circle))
print("TRAPEZIO: {0:0.3f}".format(trapezium))
print("QUADRADO: {0:0.3f}".format(square))
print("RETANGULO: {0:0.3f}".format(rect))



