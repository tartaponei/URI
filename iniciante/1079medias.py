n = int(input(""))

for i in range(n):
    x = input("").split()
    a = float(x[0])
    b = float(x[1])
    c = float(x[2])

    r = (a * 2 + b * 3 + c * 5) / 10

    print(round(r, 1))
