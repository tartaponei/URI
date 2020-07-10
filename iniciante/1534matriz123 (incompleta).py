#incompleto, ta dando erro na hora de modificar o valor da diagonal sei la pq vo chora
n = int(input(""))

matriz = []
linha = []
for i in range(n):
    linha.append(3)
    matriz.append(linha)
print(matriz)

for i in range(0, n):
    for j in range(0, n):
        print(i)
        print(j)
        if(i == j):
            matriz[i][j] = 1
        print(matriz)
for i in range(n):
    print(matriz[i])
