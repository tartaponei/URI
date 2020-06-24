a = True
while(a == True):
    s = input("").split()
    x = int(s[0])
    y = int(s[1])

    if(x != y):
        if(x < y):
            print("Crescente")
        else:
            print("Decrescente")
    else:
        break
