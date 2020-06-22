valor = input("").split('.')
n = int(valor[0])
m = int(valor[1])

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

moe1 = int(n / 1)
if(moe1 > 0):
    n = n -(moe1 * 1)

moe50 = int(m / 50)
if(moe50 > 0):
    m = m - (moe50 * 50)

moe25 = int(m / 25)
if(moe25 > 0):
    m = m - (moe25 * 25)

moe10 = int(m / 10)
if(moe10 > 0):
    m = m - (moe10 * 10)

moe5 = int(m / 5)
if(moe5 > 0):
    m = m - (moe5 * 5)

moe01 = int(m / 1)
if(moe01 > 0):
    m = m - (moe01 * 1)

print("NOTAS:")
print(ced100, "nota(s) de R$ 100.00")
print(ced50, "nota(s) de R$ 50.00")
print(ced20, "nota(s) de R$ 20.00")
print(ced10, "nota(s) de R$ 10.00")
print(ced5, "nota(s) de R$ 5.00")
print(ced2, "nota(s) de R$ 2.00")
print("MOEDAS:")
print(moe1, "moeda(s) de R$ 1.00")
print(moe50, "moeda(s) de R$ 0.50")
print(moe25, "moeda(s) de R$ 0.25")
print(moe10, "moeda(s) de R$ 0.10")
print(moe5, "moeda(s) de R$ 0.05")
print(moe01, "moeda(s) de R$ 0.01")
