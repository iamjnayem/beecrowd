while True:
    x, y = map(int,input().split())
    if x <= 0 or y <= 0:
        break 
    
    if x > y:
        temp = x
        x = y
        y = temp 
    sum = 0
    for i in range(x, y+1):
        print(i,end=" ")
        sum += i 
    print(f"Sum={sum}")
    