qt = int(input(""))

for i in range(qt):
    jog = input("").split()
    j1 = jog[0]
    e1 = jog[1]
    j2 = jog[2]
    e3 = jog[3]

    num = input("").split()
    n = int(num[0])
    m = int(num[1])

    if((n+m) % 2 == 0):
        if(e1 == 'PAR'):
            print(j1)
        else:
            print(j2)
    else:
        if(e1 == 'IMPAR'):
            print(j1)
        else:
            print(j2)
