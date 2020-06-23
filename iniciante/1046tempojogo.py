x = input("").split()
a = int(x[0])
b = int(x[1])

if(a > b):
    h = (24 - a) + b
elif(a < b):
    if(b > 12):
        h = (12 - a) + (b - 12)
    else:
        h = b - a
else:
    h = 24

print("O JOGO DUROU", h, "HORA(S)")
