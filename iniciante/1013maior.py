x = input("").split()

a = int(x[0])
b = int(x[1])
c = int(x[2])

maior1 = int((a + b + abs(a - b)) / 2)
maior = int((maior1 + c + abs(maior1 - c)) / 2)

print(maior, "eh o maior")
