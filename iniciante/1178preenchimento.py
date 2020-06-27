x = float(input(""))
n = []

for i in range(100):
    n.append(x)

    print("N[{}] = {:.4f}" .format(i, x))
    x = x/2
