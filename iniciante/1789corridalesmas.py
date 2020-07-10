while True:
    try:
        l = int(input(""))
        lesmas = []
        s = input("").split()
        for i in range(l):
            lesmas.append(int(s[i]))
            
        if(max(lesmas) < 10):
            print("1")
        elif(max(lesmas) >= 10 and max(lesmas) < 20):
            print("2")
        else:
            print("3")
            
    except EOFError:
        break
