#dá resposta errada, depois refaço
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

dias, horas, minutos, segundos = 0, 0, 0, 0

if(horai == horaf and minutoi == minutof and segundoi == segundof):
    dias = diaf - diai
else:
    dias = diaf - diai - 1
    if(segundof >= segundoi):
        segundos = segundof - segundoi
    else:
        segundos = 60 - (segundoi - segundof)

    if(minutof >= minutoi):
        minutos = minutof - minutoi
    else:
        minutos = 60 -(minutoi - minutof)

    if(horaf >= horai):
        horas = horaf - horai
    else:
        horas = 24 -(horai - horaf)

print(dias, "dia(s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")
