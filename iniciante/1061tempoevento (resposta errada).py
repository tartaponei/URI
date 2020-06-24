#tbm dá resposta errada não sei pq jesus amado
x = input("").split()
diai = int(x[1])

y = input("").split(" : ")
horai = int(y[0])
minutoi = int(y[1])
segundoi = int(y[2])

x = input("").split()
diaf = int(x[1])

y = input("").split(" : ")
horaf = int(y[0])
minutof = int(y[1])
segundof = int(y[2])

dias = diaf - diai - 1

if(horaf < horai):
    horas = 24 - (horai - horaf)
else:
    horas = abs(horaf - horai)

if(minutoi > minutof):
    minutos = abs(60 - (minutoi - minutof))
    horas -= 1
else:
    minutos = minutof - minutoi

if(segundoi > segundof):
    segundos = abs(60 - (segundoi - segundof))
    minutos -= 1
else:
    segundos = segundof - segundoi

print(dias, "dia(s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")








    

