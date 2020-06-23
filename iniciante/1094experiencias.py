n = int(input(""))
totalsapo, totalcoelho, totalrato, total = 0, 0, 0, 0
persapo, percoelho, perrato = 0, 0, 0

for i in range(n):
    x = input("").split()
    quantia = int(x[0])
    tipo = x[1]

    total = total + quantia
    
    if(tipo == "C"):
        totalcoelho = totalcoelho + quantia
    elif(tipo == "R"):
        totalrato = totalrato + quantia
    elif(tipo == "S"):
        totalsapo = totalsapo + quantia

print("Total:", total, "cobaias")
print("Total de coelhos:", totalcoelho)
print("Total de ratos:", totalrato)
print("Total de sapos:", totalsapo)
print("Percentual de coelhos: {:.2f} %" .format(round((100*totalcoelho)/total, 2)))
print("Percentual de ratos: {:.2f} %" .format(round((100*totalrato)/total, 2)))
print("Percentual de sapos: {:.2f} %" .format(round((100*totalsapo)/total, 2)))
