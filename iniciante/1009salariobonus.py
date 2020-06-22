nome = input("")
salario = float(input(""))
vendas = float(input(""))

bonus = vendas * 0.15

print("TOTAL = R$ {:.2f}" .format(salario + bonus))
