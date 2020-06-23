#refiz mas ainda dá errado aaaaaa
#uri eu te odeio
x = input("").split()
hi = int(x[0])
mi = int(x[1])
hf = int(x[2])
mf = int(x[3])

if(hi == hf and mi == mf):
    minutos = 0
    horas = 24
else:
    if(hi >= 12):
        horas = (24 - hi) + hf
    else:
        horas = abs(hf - hi)
        
    minutos = mi - mf

    if(minutos > 0):
        horas-= 1
        minutos = abs(60 - minutos)

print("O JOGO DUROU", horas, "HORA(S) E", abs(minutos), "MINUTO(S)")
