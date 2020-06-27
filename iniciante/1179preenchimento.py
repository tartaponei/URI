par = []
impar = []

for i in range(15):
    x = int(input(""))

    if(x % 2 == 0):
        par.append(x)
        if(len(par) == 5):
            for i in range(len(par)):
                print("par[{}] = {}" .format(i, par[i]))
            par.clear()
    else:
        impar.append(x)
        if(len(impar) == 5):
            for i in range(len(impar)):
                print("impar[{}] = {}" .format(i, impar[i]))
            impar.clear()

for i in range(len(impar)):
    print("impar[{}] = {}" .format(i, impar[i]))

for i in range(len(par)):
    print("par[{}] = {}" .format(i, par[i]))
