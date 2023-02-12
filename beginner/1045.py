a, b, c = map(float, input().split(' '))

if a < b:
    temp = a 
    a = b 
    b = temp 

if b < c:
    temp = b
    b = c 
    c = temp 

if a < b:
    temp = a 
    a = b 
    b = temp 


if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if a*a == b*b + c*c:
        print("TRIANGULO RETANGULO")
    if a*a > (b*b + c*c):
        print("TRIANGULO OBTUSANGULO")
    if a*a < (b*b + c*c):
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")
