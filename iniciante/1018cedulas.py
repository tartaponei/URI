n = int(input(""))
print(n)

ced100 = int(n / 100)
if(ced100 > 0):
    n = n - (ced100 * 100)

ced50 = int(n / 50)
if(ced50 > 0):
    n = n -(ced50 * 50)

ced20 = int(n / 20)
if(ced20 > 0):
    n = n -(ced20 * 20)

ced10 = int(n / 10)
if(ced10 > 0):
    n = n -(ced10 * 10)

ced5 = int(n / 5)
if(ced5 > 0):
    n = n -(ced5 * 5)

ced2 = int(n / 2)
if(ced2 > 0):
    n = n -(ced2 * 2)

ced1 = int(n / 1)
if(ced1 > 0):
    n = n -(ced1 * 1)

print(ced100, "nota(s) de R$ 100,00")
print(ced50, "nota(s) de R$ 50,00")
print(ced20, "nota(s) de R$ 20,00")
print(ced10, "nota(s) de R$ 10,00")
print(ced5, "nota(s) de R$ 5,00")
print(ced2, "nota(s) de R$ 2,00")
print(ced1, "nota(s) de R$ 1,00")
