#não sei pq nos exemplos tá que '-7 3' dá '-3 2' como saída
s = input("").split()
a = int(s[0])
b = int(s[1])

q = int(a/b)
r = a - (b*q)

print("{} {}" .format(q, r))
