n = int(input(""))

for i in range(n):
    s = input("").split()
    f1 = int(s[0])
    f2 = int(s[1])

    mdc = 1
    d = 2

    if(f1 < f2):
        menor = f1
    else:
        menor = f2

    while(d <= menor):
        if(f1 % d == 0 and f2 % d == 0):
            mdc = d
        d += 1

    print(mdc)
