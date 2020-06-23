j, x, i = 7, 4, 1

while(i <= 9):
    print("I={} J={}" .format(i, j))
    j = j - 1

    if(j == x):
        j += 5
        x = j - 3
        i += 2
