x = input("").split()
cod = int(x[0])
qtd = int(x[1])

if(cod == 1):
    print("Total: R$ {:.2f}" .format(qtd * 4))
elif(cod == 2):
    print("Total: R$ {:.2f}" .format(qtd * 4.50))
elif(cod == 3):
    print("Total: R$ {:.2f}" .format(qtd * 5))
elif(cod == 4):
    print("Total: R$ {:.2f}" .format(qtd * 2))
elif(cod == 5):
    print("Total: R$ {:.2f}" .format(qtd * 1.50))
