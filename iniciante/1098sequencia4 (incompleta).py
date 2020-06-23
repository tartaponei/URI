#incompleta
j, x, i = 1, 4, 0
s = 0

while(i <= 2):
    print("I={} J={}" .format(i, j))
    j = j + 1

    if(j == x):
        s += 1
        
        j = 1 + (0.2 * s)
        j = round(j, 1)
      
        x += 0.2
        x = round(x, 1)
        
        i += 0.2
        i = round(i, 1)
        
