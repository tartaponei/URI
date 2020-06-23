#lógica do bruno
s = float(input(""))
taxa = 0

if(s <= 2000):
    print("Isento")
else:
    s -= 2000

    if(s > 1000):
        taxa += 1000 * 0.08
        s -= 1000

        if(s > 1500):
            taxa += 1500 * 0.18
            taxa += (s - 1500) * 0.28
        else:
            taxa += s * 0.18
    else:
        taxa += s * 0.08

    print("R$ {:.2f}" .format(taxa))

"""
#essa foi a minha primeira lógica que não batia o resultado
s = float(input(""))
taxa1, taxa2, taxa3 = 0, 0, 0
if(s <= 2000):
    print("Isento")
else:
    st = s - 2000
    n = int(st/1000)
    taxa1 = 0.08 * (n*1000)

    if(s > 3000):
        st = st - (n*1000)
        if(s <= 4500):
            taxa2 = 0.18 * st
        else:
            n = int(st/100)
            taxa2 = 0.18 * (n*100)

            if(s > 4500):
                st = st - (n*100)
                taxa3 = 0.28 * st

    print("R$ {:.2f}" .format(taxa1+taxa2+taxa3))
"""
