x = 1
while(x != 0):
    x = int(input(""))
    if(x == 0):
        break
    else:
        soma = 0
        contador = 0
        
        while(contador < 5):
            if(x % 2 == 0):
                soma += x
                contador += 1
            x += 1
            
        print(soma)
