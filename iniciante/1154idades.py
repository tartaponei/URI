idades = []
x = 1
soma = 0
while(x >= 0):
    x = int(input(""))
    if(x < 0):
        break
    else:
        idades.append(x)

for i in range(len(idades)):
    soma += idades[i]

print("{:.2f}" .format(soma/len(idades)))
