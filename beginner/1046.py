a, b = map(int, input().split(' '))

if a > b:
    a = a - 12
    b = b + 12
    print("O JOGO DUROU {0} HORA(S)".format(b-a))
elif a < b:
    print("O JOGO DUROU {0} HORA(S)".format(b-a))
else:
    print("O JOGO DUROU 24 HORA(S)")