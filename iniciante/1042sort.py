x = input("").split()
for i in range(len(x)):
    x[i] = int(x[i])
y = sorted(x)

print(y[0], y[1], y[2], sep='\n')
print("")
print(x[0], x[1], x[2], sep='\n')
