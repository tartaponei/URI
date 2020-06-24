n = int(input(""))

for i in range(n):
    soma = 0
    s = input("").split()
    x = int(s[0])
    y = int(s[1])

    if(x > y):
        maior, menor = x, y
    else:
        maior, menor = y, x

    for i in range(menor+1, maior):
        if(i % 2 != 0):
            soma += i

    print(soma)
