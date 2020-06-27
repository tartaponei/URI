t = int(input(""))
n = []
x = 0

for i in range(1000):
    n.append(x)

    print("N[{}] = {}" .format(i, x))
    x += 1

    if(x == t):
        x = 0
