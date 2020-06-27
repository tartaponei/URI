#pq o nome é "fibonacci em vetor" se não precisa de vetor?
t = int(input(""))

for i in range(t):
    n = int(input(""))
    proximo = 0
    anterior = 0
    s = ""

    for j in range(n):
       proximo = proximo + anterior
       anterior = proximo - anterior
       
       if(proximo == 0):
           proximo = proximo + 1
           
    print("Fib({}) = {}" .format(n, proximo))
