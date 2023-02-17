n = int(input())
total = 0
totalC = 0
totalR = 0
totalS = 0


for i in range(n):
    amount, name = input().split(" ")
    amount = int(amount.strip())
    name = name.strip()

    total += amount 

    if name == "C":
        totalC += amount 
    
    if name == "R":
        totalR += amount
    
    if name == "S":
        totalS += amount 

cPer = (totalC/total)*100
rPer = (totalR/total)*100
sPer = (totalS/total)*100


print("Total: {0} cobaias".format(total))
print("Total de coelhos: {0}".format(totalC))
print("Total de ratos: {0}".format(totalR))
print("Total de sapos: {0}".format(totalS))
print("Percentual de coelhos: {0:0.2f} %".format(cPer))
print("Percentual de ratos: {0:0.2f} %".format(rPer))
print("Percentual de sapos: {0:0.2f} %".format(sPer))