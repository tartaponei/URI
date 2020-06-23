p = 0
s = 0
for i in range(6):
    n = float(input(""))
    if(n > 0):
        p += 1
        s = s + n
print(p, "valores positivos")
print("{:.1f}" .format(s / p))
