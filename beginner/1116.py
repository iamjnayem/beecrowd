testcase = int(input())
while testcase > 0:
    a, b = map(int, input().split(' '))
    try:
        result = a / b
        print(f"{result:0.1f}")
    except ZeroDivisionError:
        print("divisao impossivel")
        
    testcase -= 1

    