#tbm dá resposta errada não sei pq
x = input("").split()
hi = int(x[0])
mi = int(x[1])
hf = int(x[2])
mf = int(x[3])

if(hi == hf and hi == mi and mi == mf):
    hd = 24
    md = 0

elif(hf > hi and mf > mi):
    hd = hf - hi
    md = mf - mi

elif(hf == hi + 1 and mf < mi):
    hd = 0
    md = int(((mi * 60) - (mf * 60)) / 60)
    if(md == 1):
        md = 59

print("O JOGO DUROU", hd, "HORA(S) E", md, "MINUTO(S)")
