a = input("").split()
x = int(a[0])
y = int(a[1])
i = 1
while(i < y+1):
    s = ""
    for j in range(x):
        s = s + str(i) + " "
        i+=1
    print(s.rstrip())
