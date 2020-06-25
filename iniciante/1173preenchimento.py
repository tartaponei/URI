n = []
v = int(input(""))
n.append(v)

for i in range(1, 10):
    n.append(n[i-1] * 2)

for i in range(10):
    print("N[{}] = {}" .format(i, n[i]))
