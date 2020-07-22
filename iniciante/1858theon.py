#não sei pq dá wrong answer
n = int(input(""))
s = input("")
v = []

for i in range((n*2)-1):
    v.append(s[i])
    
a = []
for i in range(len(v)):
    if(v[i] != ' '):
        a.append(v[i])
        
menor = a[0]
posicao = 1
for i in (1, len(a)-1):
    if(a[i] < menor):
        menor = a[i]
        posicao = i+1

print(posicao)
    
