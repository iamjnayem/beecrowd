stop = 1
score_list = []
calculated = False

while stop != 2:
    score = float(input())
    if score < 0 or score > 10:
        print("nota invalida")
        continue
    else:
        score_list.append(score)

    if len(score_list) == 2:
        avg = (score_list[0] + score_list[1])/2
        print(f"media = {avg:0.2f}")
        score_list = []
        calculated = True
    else:
        calculated = False

    while calculated:
        print("novo calculo (1-sim 2-nao)")
        res = int(input())
        if res != 1 and res != 2:
            continue
        else:
            if res == 1:
                calculated = False
                break
            else:
                stop = 2
                break



