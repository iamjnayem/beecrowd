a, b, c = map(int, input().split(' '))

x, y, z = a, b, c 



if x > y:
    temp = x 
    x = y 
    y = temp 


if y > z:
    temp = y 
    y = z
    z = temp 


if x > y:

    temp = x 
    x = y 
    y = temp 

print(x)
print(y)
print(z)
print()
print(a)
print(b)
print(c)


