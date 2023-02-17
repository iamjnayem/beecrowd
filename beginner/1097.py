i = 1
j = 7
while i <= 9:
    c = 1
    temp = j
    while c <= 3:
        print("I={0} J={1}".format(i,j))
        j = j - 1
        c = c + 1
    j = temp + 2
    i = i + 2
    