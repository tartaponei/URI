#que caralho de questao é essa?
n = int(input(""))
s = ""
j = 1

for i in range(1, n+1):
    for p in range(1, 4):
        s = s + str(j) + " "
        j +=1
    s = s + "PUM"
    print(s)
    s = ""
    j += 1
