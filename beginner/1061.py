sd = input().split(" ")[1]
sh, sm, ss = input().split(" : ")

ed = input().split(" ")[1]
eh, em, es = input().split(" : ")

sd = int(sd.strip())
sh = int(sh.strip())
sm = int(sm.strip())
ss = int(ss.strip())

ed = int(ed.strip())
eh = int(eh.strip())
em = int(em.strip())
es = int(es.strip())


fs = None
fm = None
fh = None
fd = None

if es < ss:
    fs = (es + 60) - ss
    sm = sm + 1
else: 
    fs = es - ss



if em < sm:
    fm = (em+60) - sm
    sh = sh + 1
else:
    fm = em - sm

if eh < sh:
    fh = (eh + 24) - sh
    sd = sd + 1
else: 
    fh = eh - sh


fd = ed - sd

print("{0} dia(s)".format(fd))
print("{0} hora(s)".format(fh))
print("{0} minuto(s)".format(fm))
print("{0} segundo(s)".format(fs))
