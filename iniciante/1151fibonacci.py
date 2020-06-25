#eu não sei função recursiva até hojekkkkkk eu sou uma piada
n = int(input(""))
proximo = 0
anterior = 0
s = ""

for i in range(n):
   s = s + str(proximo) + " "
   proximo = proximo + anterior
   anterior = proximo - anterior
   
   if(proximo == 0):
       proximo = proximo + 1

print(s.rstrip())
