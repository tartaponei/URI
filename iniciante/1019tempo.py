n = int(input(""))
hf, mf, = 0, 0
a = 0

s = n / 60
#s = str(s).split(".")

if(n > 60):
    m = s / 60
    m = str(m).split(".")
    if(int(m[0]) > 60):
        h = m / 60
        h = str(h).split(".")
        a = 1

if(a == 1):
    hf = int(h[0])
print(hf)
sobramin = int(h[1])
mf = int(m[0] - (hf * 60))
print(mf)
sobraseg = int(m[1])

sobraseg = sobraseg + (sobramin / 60)
print(sobraseg)

#print("{}:{}:{}" hf, mf, sf)
