nimet = set()
nimi = input('Syötä nimi tai lopeta toiminta painamalla Enter:')
while nimi != '':
    if nimi in nimet:
        print('Tämä nimi on jo syötetty!')
        nimi = input('Syötä nimi tai lopeta toiminta painamalla Enter:')
    else:
        nimet.add(nimi)
        print('Tämä on uusi nimi!')
        nimi = input('Syötä nimi tai lopeta toiminta painamalla Enter:')
else:
    for p in nimet:
        print(p)