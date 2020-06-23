x = int(input(""))
y = int(input(""))
s = 0

if(x > y):
    maior = x
    menor = y
else:
    menor = x
    maior = y

for i in range(menor+1, maior):
    if(i % 2 != 0):
        s = s + i

print(s)
