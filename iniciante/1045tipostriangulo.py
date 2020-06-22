x = input("").split()
for i in range(len(x)):
    x[i] = float(x[i])

x = sorted(x, reverse=True)
a = x[0]
b = x[1]
c = x[2]

if(a >= (b + c)):
    print("NAO FORMA TRIANGULO")
else:
    if((a ** 2) == (b ** 2) + (c ** 2)):
        print("TRIANGULO RETANGULO")
    if((a ** 2) > (b ** 2) + (c ** 2)):
         print("TRIANGULO OBTUSANGULO")
    if((a ** 2) < (b ** 2) + (c ** 2)):
        print("TRIANGULO ACUTANGULO")
    if(a == b and a == c and c == b):
        print("TRIANGULO EQUILATERO")
    if((a == b and b == a and c != a and c != b) or (c == b and b == c and a != c and a != b) or (a == c and c == a and b != a and b != c)):
       print("TRIANGULO ISOSCELES")
