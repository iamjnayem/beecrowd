stop = 1
count_matches = 0
v_inter = 0
v_gremio = 0
draw = 0

while stop != 2:
    inter, gremio = map(int, input().split(' '))
    count_matches += 1
    if inter > gremio:
        v_inter += 1
    elif gremio > inter:
        v_gremio += 1
    else:
        draw += 1

    print("Novo grenal (1-sim 2-nao)")
    res = int(input())
    if res == 2:
        stop = 2
        break
    else:
        continue

print(f"{count_matches} grenais")
print(f"Inter:{v_inter}")
print(f"Gremio:{v_gremio}")
print(f"Empates:{draw}")
if v_inter > v_gremio:
    print("Inter venceu mais")
elif v_gremio  > v_inter:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")

