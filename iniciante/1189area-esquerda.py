o = input("")
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
    del(coluna[0])
    del(coluna[:i])
    del(coluna[-1-i:])
    
    for j in range(len(coluna)):
        soma += coluna[j]
        contador += 1
        
if(o == 'S'):
    print("{:.1f}" .format(soma))

elif(o == 'M'):
    print("{:.1f}" .format(soma/contador))
