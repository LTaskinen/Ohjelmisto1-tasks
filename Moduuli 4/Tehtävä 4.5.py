tunnus = 'python'
salasana = 'rules'
ktunnus = input('Käyttäjätunnus:')
ksalasana = input('Salasana:')
kerrat = 1
while salasana != ksalasana or tunnus != ktunnus:
    if kerrat == 5:
        print('Pääsy evätty.')
        break
    else:
        kerrat = kerrat + 1
        ktunnus = input('Käyttäjätunnus:')
        ksalasana = input('Salasana:')
else:
    print('Tervetuloa!')