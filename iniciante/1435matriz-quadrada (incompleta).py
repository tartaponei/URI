#incompleta
n = 1
while(n != 0):
    n = int(input(""))
    #s = "  "
    if(n % 2 == 0):
        a = n/2
    else:
        a = n/2 + 1
        
    for i in range(int(a)):
        print(i)
        linha = []
        coluna = []
        for b in range(n):
                linha.append(1)
                
        if(i == 0 or i == n-1):
            s = "  "
            for j in range(n):
                s += str(linha[j]) + "   "
            print(s.rstrip())

        elif(i == n-1):
            s = "\n  "
            for j in range(n):
                s += str(linha[j]) + "   "
            print(s.rstrip())
            
        else:
            #print(linha)
            for h in range(1, n-1):
                for p in range(h, n-h):
                    #print(h)
                    linha[p] = h+1
                    #print(linha)
                
            #for j in range(n):
                #linha[j] = j+1

            #a = 0
            #for u in range(n-1, int(n/2)-1, -1):
                #linha[u] = 1 + a
                #a+=1

                s = "\n  "
                for y in range(n):
                    s += str(linha[y]) + "   "
                print(s.rstrip())

    #print(s.rstrip())
            
"""n = 1
while(n != 0):
    n = int(input(""))
    if(n == 0):
        break
    else:
        for i in range(n):
            linha = []
            for j in range(n):
                linha.append(1)
        s = "  "
        for i in range(n):
            s += str(linha[i]) + "   "

        for i in range(n):
            if(i == 0):
                print(s.rstrip())
                
            elif(i == n-1):
                st = "\n  " + s
                print(st.rstrip())

            else:  
                for j in range(1, n):
                    for p in range(j, n-j):
                        linha[p] = j+1
                    #linha[n:-n] = n+1
                st = "\n  " + s
                print(st.rstrip())"""
