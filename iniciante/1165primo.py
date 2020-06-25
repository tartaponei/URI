n = int(input(""))

for i in range(n):
    x = int(input(""))
    divisores = 1
    
    for i in range(2, x+1):
        if(x % i == 0):
            divisores += 1

    if(divisores > 2):
        print(x, "nao eh primo")
    else:
        print(x, "eh primo")
