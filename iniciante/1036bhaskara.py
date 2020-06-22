x = input("").split()
a = float(x[0])
b = float(x[1])
c = float(x[2])

delta = (b ** 2) - (4 * a * c)

if(delta < 0 or a == 0):
    print("Impossivel calcular")

else:
    print("R1 = {:.5f}" .format(((b * -1) + (delta ** (1/2))) / (2 * a)))
    print("R2 = {:.5f}" .format(((b * -1) - (delta ** (1/2))) / (2 * a)))
