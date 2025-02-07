import math
def laskenta(halkaisija, hinta):
    r = halkaisija//2
    pinta_ala1 = math.pi*r**2
    pinta_ala2 = pinta_ala1/1000
    arvo = hinta/pinta_ala2
    print(f'Pizzan euro/neliömetri hinta on:{arvo}')
    return arvo
halk1= float(input('Syötä ensimmäisen pizzan halkaisija cm:'))
hinta1= float(input('Syötä ensimmäisen pizzan hinta euroina:'))
pizza1 = laskenta(halk1, hinta1)
halk2 = float(input('Syötä toisen pizzan halkaisija cm:'))
hinta2 = float(input('Syötä toisen pizzan hinta euroina:'))
pizza2 = laskenta(halk2, hinta2)
if pizza1 > pizza2:
    print(f'Toisella pizzalla on parempi arvo per neliömetri.\n'
          f'Arvolla: {pizza2}')
else:
    print(f'Ensimmäisellä pizzalla on parempi arvo per neliömetri. \n'
          f'Arvolla: {pizza1}')