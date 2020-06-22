x = input("").split()
a = float(x[0])
b = float(x[1])
c = float(x[2])

if(a < (b + c) and a > abs(b - c) and b < (a + c) and b > abs(a - c) and c < (b + a) and c > abs(b - a)):
    print("Perimetro = {:.1f}" .format(a + b + c))
else:
    print("Area = {:.1f}" .format(((a+b) * c) / 2))
