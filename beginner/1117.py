score_list = []

while True:
    score = float(input())
    if score < 0 or score > 10:
        print("nota invalida")
        continue
    else:
        score_list.append(score)

    if len(score_list) == 2:
        avg = (score_list[0] + score_list[1])/2
        print(f"media = {avg:0.2f}")
        break


