n = int(input(""))
s = ""

for i in range(n):
    x = int(input(""))
    if(x == 0):
        s = "NULL"
    else:
        if(x % 2 == 0):
            s = s + "EVEN "
        else:
            s = s + "ODD "

        if(x > 2):
            s = s + "POSITIVE"
        else:
            s = s + "NEGATIVE"
    print(s)
    s = ""
