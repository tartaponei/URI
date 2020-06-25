x = 1
while(x != 0):
    x = int(input(""))

    if(x == 0):
        break
    else:
        s = ""
        for i in range(1, x+1):
            s = s + str(i) + " "
        print(s.rstrip())
