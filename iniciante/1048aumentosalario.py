s = float(input(""))

if(s > 0 and s <= 400):
    reajuste = s * 0.15
    p = 15
elif(s > 400 and s <= 800):
    reajuste = s * 0.12
    p = 12
elif(s > 800 and s <= 1200):
    reajuste = s * 0.10
    p = 10
elif(s > 1200 and s <= 2000):
    reajuste = s * 0.07
    p = 7
else:
    reajuste = s * 0.04
    p = 4

s = reajuste + s

print("Novo salario: {:.2f}" .format(s))
print("Reajuste ganho: {:.2f}" .format(reajuste))
print("Em percentual:", p, "%")
