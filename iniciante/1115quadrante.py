a = True
while(a == True):
    s = input("").split()
    x = float(s[0])
    y = float(s[1])

    if(x != 0 and y != 0):
        if(x > 0 and y > 0):
            print("primeiro")
        elif(x < 0 and y > 0):
            print("segundo")
        elif(x < 0 and y < 0):
            print("terceiro")
        elif(x > 0 and y < 0):
            print("quarto")
    else:
        break
