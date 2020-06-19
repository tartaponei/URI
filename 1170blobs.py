n = int(input(""))

for i in range(n):
    c = float(input(""))
    i = 0

    while(c > 1):
        c = c / 2
        i+=1

    print(i, "dias")
