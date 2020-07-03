l = int(input(""))
t = input("")
m = []

for i in range(12):
    linha = []
    for j in range(12):
        a = float(input(""))
        linha.append(a)
    m.append(linha)

soma = 0
for i in range(12):
    soma += m[l][i]
        
if(t == 'S'):
    print("{:.1f}" .format(soma))

elif(t == 'M'):
    print("{:.1f}" .format(soma/12))
