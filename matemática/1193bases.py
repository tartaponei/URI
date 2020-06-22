def bina(x):
    r = 1
    b = ""
    while(x >= 1):
        r = x % 2
        b = b + str(r)
        x = int(x / 2)
    return b[::-1]

def hexa(x):
    r = 1
    h = ""
    if(x > 15):
        while(int(x / 16) >= 0):
            r = x % 16
            if(r > 9):
                if(r == 10):
                    r = "A"
                elif(r == 11):
                    r = "B"
                elif(r == 12):
                    r = "C"
                elif(r == 13):
                    r = "D"
                elif(r == 14):
                    r = "E"
                elif(r == 15):
                    r = "F"
            h = h + str(r)
            x = int(x / 16)
            if(x == 0):
                break
        return h[::-1]
    else:
        return x
    
    
n = int(input(""))

for i in range(n):
    s = input("").split()
    x = s[0]
    y = s[1]

    a = "Case " + str(i+1) + ":"

    if(y == "bin"):
        print(a)
        print(int(x, 2), "dec")
        print(hexa(int(x, 2)), "hex")
        print(" ")
    
    elif(y == "hex"):
        print(a)
        print(int(x, 16), "dec")
        print(bina(int(x, 16)), "bin")
        print(" ")
        
    else:
        print(a)
        print(hexa(int(x)), "hex")
        print(bina(int(x)), "bin")
        print(" ")
