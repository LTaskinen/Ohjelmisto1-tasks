def muunnos (bensa):
    litrat = bensa * 3.785
    return litrat
while True:
    print('Ohjelma lopettaa toiminnan jos syötät negatiivisen luvun.')
    luku = float(input('Syötä gallonamäärä:'))
    while luku > 0:
        l = muunnos(luku)
        print(f'{luku}gallonaa on litroina: {l}litraa')
        luku = float(input('Syötä uusi gallonamäärä:'))
    else:
        break