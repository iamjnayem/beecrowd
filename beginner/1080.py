max = -2147483648
j = None 
for i in range(1, 101):
    x = int(input())
    if x > max:
        max = x 
        j = i 

print(max)
print(j)