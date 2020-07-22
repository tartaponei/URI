#incompleta (só funciona usando o menornúmero como um dos lados)
s = input("").split()

a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

contador = 0

v = [a, b, c, d]

menor = min(v)

for i in range(len(v)):
    if(v[i] == menor):
        del(v[i])
        break

if(v[0] <= menor + v[1] and v[1] <= menor + v[0]):
    print('S')
elif(v[1] <= menor + v[2] and v[2] <= menor + v[1]):
    print('S')
elif(v[0] <= menor + v[2] and v[2] <= menor + v[0]):
    print('S')
else:
    print('N')
