n1, n2, n3, n4 = [float(x) for x in input().split(' ')]

average = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/(2 + 3 + 4 + 1)

print("Media: {0:0.1f}".format(average))
if average >= 7.0:
    print("Aluno aprovado.")
elif average < 5.0:
    print("Aluno reprovado.")
elif average >= 5.0 and average <= 6.9:
    print("Aluno em exame.")
    print("Nota do exame: ", end="")
    extraScore = float(input())
    reCalculatedAverage = (average + extraScore) / 2.0
    if reCalculatedAverage >= 5.0:
        print("Aluno aprovado.")
        print("Media final: {0:0.1f}".format(reCalculatedAverage))
    if reCalculatedAverage <= 4.9:
        print("Aluno reprovado.")
        print("Media final: {0:0.1f}".format(reCalculatedAverage))
