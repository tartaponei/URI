n = int(input(""))

for i in range(n):
    s = input("").split()
    x = int(s[0])
    y = int(s[1])

    if(y == 0):
        print("divisao impossivel")
    else:
        print(x/y)
