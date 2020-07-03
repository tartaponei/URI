t = input("")
m = []

for i in range(12):
    linha = []
    for j in range(12):
        a = float(input(""))
        linha.append(a)
    m.append(linha)

soma = 0
contador = 0
for i in range(12):
    coluna = []
    for p in range(12):
        coluna.append(m[p][i])
    del(coluna[-1])
    if(i > 0):
        del(coluna[11-i:])

    for j in range(len(coluna)):
        soma += coluna[j]
        contador += 1
        
if(t == 'S'):
    print("{:.1f}" .format(soma))

elif(t == 'M'):
    print("{:.1f}" .format(soma/contador))
