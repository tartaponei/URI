t = int(input(""))

for i in range(t):
    s = input("").split()
    pa = int(s[0])
    pb = int(s[1])
    g1 = float(s[2])
    g2 = float(s[3])

    contador = 1
    while(pb >= pa):
        a = pa * (g1/100)
        pa = pa + int(a)
        b = pb * (g2/100)
        pb = pb + int(b)

        if(pa <= pb):
            contador += 1
        else:
            break
        
        if(contador > 100):
            break

    if(contador > 100):
        print("Mais de 1 seculo.")
    else:
        print(contador, "anos.")
    
