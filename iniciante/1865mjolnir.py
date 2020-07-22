c = int(input(""))

for i in range(c):
    s = input("").split()
    nome = s[0]

    if(nome == "Thor"):
        r = 'Y'
    else:
        r = 'N'
    print(r)
