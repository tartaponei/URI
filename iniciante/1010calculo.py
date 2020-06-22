item1 = input("").split()
item2 = input("").split()

codigo1 = item1[0]
num1 = int(item1[1])
valor1 = float(item1[2])
codigo2 = item2[0]
num2 = int(item2[1])
valor2 = float(item2[2])

print("VALOR A PAGAR: R$ {:.2f}" .format((num1 * valor1) + (num2 * valor2)))
