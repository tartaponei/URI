x = int(input(""))
y = int(input(""))

if(x > y):
    maior, menor = x, y
else:
    maior, menor = y, x

for i in range(menor+1, maior):
    if(i % 5 == 2 or i % 5 == 3):
        print(i)
