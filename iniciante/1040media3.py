x = input("").split()
n1 = float(x[0])
n2 = float(x[1])
n3 = float(x[2])
n4 = float(x[3])

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print("Media: {:.1f}" .format(media))

if(media >= 7):
    print("Aluno aprovado.")
elif(media < 5):
    print("Aluno reprovado.")
else:
    
    print("Aluno em exame.")
    e = float(input(""))
    print("Nota do exame: {:.1f}" .format(e))

    media = (media + e) / 2
    
    if(media >= 5):
        print("Aluno aprovado.")
    elif(media < 5):
        print("Aluno reprovado.")

    print("Media final: {:.1f}" .format(media))
