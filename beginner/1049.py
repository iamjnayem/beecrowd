l1 = input()
l2 = input()
l3 = input()

if l1 == "vertebrado":
    if l2 == "ave":
        if l3 == "carnivoro":
            print("aguia")
        elif l3 == "onivoro":
            print("pomba")  
    elif l2 == "mamifero":
        if l3 == "onivoro":
            print("homem")
        elif l3 == "herbivoro":
            print("vaca") 
elif l1 == "invertebrado":
    if l2 == "inseto":
        if l3 == "hematofago":
            print("pulga")
        elif l3 == "herbivoro":
            print("lagarta")
    elif l2 == "anelideo":
        if l3 == "hematofago":
            print("sanguessuga")
        elif l3 == "onivoro":
            print("minhoca") 
