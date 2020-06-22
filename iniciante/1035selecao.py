x = input("").split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])

if(b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0):
    print("Valores aceitos")

else:
    print("Valores nao aceitos")
