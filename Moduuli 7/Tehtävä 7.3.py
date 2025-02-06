def uusi():
    icao1 = input('Syötä uuden aseman ICAO-koodi:')
    unimi = input('Syötä uuden aseman nimi:')
    asematiedot[icao1] = unimi
    return asematiedot

def etsintä():
    enimi = input('Mikä on lentokentän ICAO-koodi?:')
    if enimi in asematiedot:
        print(f'ICAO-koodi:{enimi} on lentokenttä: {asematiedot[enimi]}')
asematiedot = {}

print('Tervetuloa!')
while True:
    user1 = input('Jos haluat syöttää uuden lentoaseman syötä: a\n'
                    'Jos haluat etsiä lentoaseman tiedot syötä: b\n'
                    'Jos haluat lopettaa toiminnan syötä tyhjä vastaus:').lower()
    if user1 == 'a':
        uusi()
    elif user1 == 'b':
        etsintä()
    else:
        print('lopetit toiminnan')
        break
