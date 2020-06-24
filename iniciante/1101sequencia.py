#dá errado não sei onde, tiraram do cu
a = True

while(a == True):
    s = ""
    soma = 0
    x = input("").split()
    m = int(x[0])
    n = int(x[1])
    
    if(m != 0 and n != 0):
        if(m > n):
            maior, menor = m, n
        else:
            maior, menor = n, m

        for i in range(menor, maior+1):
            s = s + str(i) + " "
            soma = soma + i

        s = s + "Sum={}" .format(soma)
        
        print(s)
    else:
        break
