#dá resposta errada não sei pq
n = int(input(""))
x = []

s = input("").split()
for i in range(n):
    x.append(s[i])

menor = x[0]
posicao = 0

for i in range(n):
    if(x[i] < menor):
        menor = x[i]
        posicao = i

print("Menor valor:", menor)
print("Posicao:", posicao)
