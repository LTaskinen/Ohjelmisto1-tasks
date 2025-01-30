def summa(lista):
    lsumma = sum(lista)
    return lsumma
lista1 = []
while True:
    luku = input('Anna luku tai lopeta painamalla enter:')
    while luku != '':
        luku = int(luku)
        lista1.append(luku)
        luku = input('Anna toinen luku tai lopeta painamalla enter:')
    else:
        s = summa(lista1)
        print(f'Lukujen summa on: {s}')
        break