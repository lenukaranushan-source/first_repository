dec = int(input("Entrez le nombre décimal à convertir."))
calcul = dec
quotient = 0
reste = 0
num = 0
# Quotient : // ; Reste : %
while calcul >= 0:
    quotient = dec // 2
    reste = dec % 2
    num += 1
    res = str(reste)*num
    calcul = dec/2
print(res)