
list = []
for i in range(10, 21):
    list.append(i)

dict = {}
for i in range(11):
    dict[list[i]] = True 

testCase = int(input())
inRange = 0
outRange = 0

for x in range(testCase):
    num = int(input())
    if dict.get(num):
        inRange += 1
    else:
        outRange += 1

print("{0} in".format(inRange))
print("{0} out".format(outRange))

