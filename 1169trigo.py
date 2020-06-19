n = int(input(""))

for i in range(n):
    x = int(input(""))

    if(((2 ** x) / 12000) >= 0):
        print(int((2 ** x) / 12000), "kg")
