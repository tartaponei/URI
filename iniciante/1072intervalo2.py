n = int(input(""))
i = 0
o = 0

for p in range(n):
    x = int(input(""))
    if(x >= 10 and x <= 20):
        i = i + 1
    else:
        o = o + 1

print(i, "in")
print(o, "out")
