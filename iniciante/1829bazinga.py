#dá resposta errada não sei pq
matriz = [[3, 2, 1, 1, 2], [1, 3, 2, 2, 1], [2, 1, 3, 1, 2], [2, 1, 2, 3, 1], [2, 2, 1, 2, 3]]

t = int(input(""))

for i in range(t):
    s = input("").split()
    if(s[0] == "pedra"):
        sheldon = 0
    elif(s[0] == "papel"):
        sheldon = 1
    elif(s[0] == "tesoura"):
        sheldon = 2
    elif(s[0] == "lagarto"):
        sheldon = 3
    else:
        sheldon = 4

    if(s[1] == "pedra"):
        raj = 0
    elif(s[1] == "papel"):
        raj = 1
    elif(s[1] == "tesoura"):
        raj = 2
    elif(s[1] == "lagarto"):
        raj = 3
    else:
        raj = 4
        
    if(matriz[sheldon][raj] == 1):
        r = "Bazinga!"
    elif(matriz[sheldon][raj] == 2):
        r = "Raj trapaceou!"
    else:
        r = "De novo!"

    print("Caso #{}: {}" .format(i+1, r))
