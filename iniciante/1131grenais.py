r = 1
grenais, vitorias_inter, vitorias_gremio, empates = 0, 0, 0, 0
while(r == 1):
    x = input("").split()
    inter = int(x[0])
    gremio = int(x[1])

    if(inter > gremio):
        vitorias_inter += 1
    elif(inter < gremio):
        vitorias_gremio += 1
    else:
        empates += 1

    grenais += 1

    print("Novo grenal (1-sim 2-nao)")
    r = int(input(""))

print(grenais, "grenais")
print("Inter:{}" .format(vitorias_inter))
print("Gremio:{}" .format(vitorias_gremio))
print("Empates:{}" .format(empates))

if(vitorias_inter > vitorias_gremio):
    print("Inter venceu mais")
elif(vitorias_inter < vitorias_gremio):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
