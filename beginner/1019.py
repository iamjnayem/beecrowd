sec = int(input())

h = sec // 3600
rest = sec % 3600

m = rest // 60
rest = rest % 60

s = rest 
print("{0}:{1}:{2}".format(h, m, s))