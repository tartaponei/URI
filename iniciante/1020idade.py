n = int(input(""))

ano = int(n / 365)
n = n - (365 * ano)

mes = int(n / 30)
n = n - (30 * mes)

print(ano, "ano(s)")
print(mes, "mes(es)")
print(n, "dia(s)")
