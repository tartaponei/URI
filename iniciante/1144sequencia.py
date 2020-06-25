n = int(input(""))

for i in range(1, n+1):
    s = ""
    s = s + str(i) + " " + str(i**2) + " " + str(i**3)
    print(s)
    s = ""
    s = s + str(i) + " " + str((i**2)+1) + " " + str((i**3)+1)
    print(s)
