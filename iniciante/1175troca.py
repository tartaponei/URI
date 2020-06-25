n = []
for i in range(20):
    n.append(int(input("")))

for i in range(10):
    a = n[i]
    n[i] = n[19-i]
    n[19-i] = a
    
for i in range(20):
    print("N[{}] = {}" .format(i, n[i]))
