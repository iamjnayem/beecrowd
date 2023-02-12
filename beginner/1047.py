a, b, c, d = map(int, input().split(' '))

h = None 
m = None 

if a == b == c == d:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if d < b:
        d = d + 60
        a = a + 1
        m = d - b 
    else:
        m = d - b 

    if c < a:
        c = c + 24
        h = c - a
    else:
        h = c - a 
    print("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)".format(h,m))

