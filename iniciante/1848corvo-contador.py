contador = 0
soma = 0
while(contador < 3):
    p = input("")
    if(p == 'caw caw'):
        contador += 1
        print(soma)

        bi = 0
        soma = 0
    else:
        esquerdo = p[0]
        meio = p[1]
        direito = p[2]
        bi = ''

        if(esquerdo == '-'):
            bi += '0'
        else:
            bi += '1'
        if(meio == '-'):
            bi += '0'
        else:
            bi += '1'
        if(direito == '-'):
            bi += '0'
        else:
            bi += '1'

        soma += int(bi, 2)
