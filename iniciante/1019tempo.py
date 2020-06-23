n = int(input(""))
minutos, segundos, horas = 0, 0, 0

minutos = int(n / 60)
segundos = n - (minutos) * 60

if(n >= 3600):
    horas = int(minutos / 60)
    minutos = minutos - (horas * 60)

print("{}:{}:{}" .format(horas, minutos, segundos))
