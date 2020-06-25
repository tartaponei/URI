n = int(input(""))

for i in range(n):
    x = int(input(""))
    
    soma = 0
    for i in range(1, x):
        if(x % i == 0):
            soma += i

    if(soma == x):
        print(x, "eh perfeito")
    else:
        print(x, "nao eh perfeito")  
