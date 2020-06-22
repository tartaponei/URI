#dá resposta errada não sei pq
x = input("").split()
a = int(x[0])
b = int(x[1])

if(a == b):
    h = 24
    
elif(a > b and a > 12):
    if(a == 13):
        a = 1
    elif(a == 14):
        a = 2
    elif(a == 15):
        a = 3
    elif(a == 16):
        a = 4
    elif(a == 17):
        a = 5
    elif(a == 18):
        a = 6
    elif(a == 19):
        a = 7
    elif(a == 20):
        a = 8
    elif(a == 21):
        a = 9
    elif(a == 22):
        a = 10
    elif(a == 23):
        a = 11

    if(b == 1):
        b = 13
    elif(b == 2):
        b = 14
    elif(b == 3):
        b = 15
    elif(b == 4):
        b = 16
    elif(b == 5):
        b = 17
    elif(b == 6):
        b = 18
    elif(b == 7):
        b = 19
    elif(b == 8):
        b = 20
    elif(b == 9):
        b = 21
    elif(b == 10):
        b = 22
    elif(b == 11):
        b = 23

    h = b - a

else:
    h = b - a

print("O JOGO DUROU", h, "HORA(S)")
