n = []

for i in range(100):
    n.append(int(input("")))

for i in range(len(n)):
    if(i == 0):
        maior = n[i]
        posicao = i + 1
    else:
        if(n[i] > maior):
            maior = n[i]
            posicao = i + 1
print(maior)
print(posicao)
