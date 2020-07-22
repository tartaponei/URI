s = input("").split()
a = int(s[0])
b = int(s[1])
c = int(s[2])

if(b < a):
    if(c >= b):
        cara = ':)'
    elif(c < b and b-c < a-b):
        cara = ':)'
    else:
        cara = ':('
elif(b > a):
    if(c <= b):
        cara = ':('
    elif(c > b and c-b < b-a):
        cara = ':('
    else:
        cara = ':)'
else:
    if(c > b):
        cara = ':)'
    else:
        cara = ':('

print(cara)
