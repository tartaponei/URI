n = int(input(""))

for i in range(n):
    s = input("").split()
    x = int(s[0])
    y = int(s[1])

    soma = 0
    contador = 0
    
    while(contador < y):
        if(x % 2 != 0):
            soma += x
            contador += 1
        x += 1
        
    print(soma)
