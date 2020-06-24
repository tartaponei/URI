r = 1
while(r == 1):
    x, y = -1, -1

    while(x < 0 or x > 10):
        x = float(input(""))

        if(x < 0 or x > 10):
            print("nota invalida")

    while(y < 0 or y > 10):
        y = float(input(""))

        if(y < 0 or y >10):
            print("nota invalida")

    print("media = {:.2f}" .format((x+y)/2))
            
    r = 3
    while(r != 1 and r != 2):
        print("novo calculo (1-sim 2-nao)")
        r = int(input(""))
