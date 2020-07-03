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
    linha = m[i]
    del(linha[0])
    del(linha[:i])
    del(linha[-1-i:])

    for j in range(len(linha)):
        soma += linha[j]
        contador += 1
        
if(t == 'S'):
    print("{:.1f}" .format(soma))

elif(t == 'M'):
    print("{:.1f}" .format(soma/contador))
