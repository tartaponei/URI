#o exemplo tá errado, ele não aceita mas é isso aqui
x = int(input(""))
z = x
while(z <= x):
    z = int(input(""))

#y = z
soma = x
i = 1
contador = 2
while(soma <= z):
    soma += (soma + i)
    if(soma > z):
        break
    else:
        i += 1
        contador += 1

print(contador)
