def summa(lista):
    paritonlista = [i for i in lista if i % 2 == 0]
    return paritonlista
lista1 = []
while True:
    luku = input('Anna luku tai lopeta painamalla enter:')
    while luku != '':
        luku = int(luku)
        lista1.append(luku)
        luku = input('Anna toinen luku tai lopeta painamalla enter:')
    else:
        lista2 = summa(lista1)
        print(f'Alkuperäinen lista: {lista1}')
        print(f'Lista ilman parillisia lukuja: {lista2}')
        break