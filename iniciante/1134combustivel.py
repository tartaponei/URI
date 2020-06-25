r = 5
alcool = 0
gasolina = 0
diesel = 0
while(r < 1 or r > 4):
    c = 5
    while(c < 1 or c > 4):
        c = int(input(""))

    if(c == 1):
        alcool += 1
    elif(c == 2):
        gasolina += 1
    elif(c  == 3):
        diesel += 1
    else:
        break

print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)
