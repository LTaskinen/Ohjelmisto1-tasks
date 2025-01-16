sukupuoli = input('Minkä sukupuolinen olet?').upper()
arvo = float(input('Mikä on teidän hemoglobiiniarvo?'))
if sukupuoli == 'MIES':
    if arvo < 134:
        print('Hemoglobiini arvo on alhainen.')
    elif arvo > 195:
        print('Hemoglobiiniarvo on korkea.')
    else:
        print('Hemoglobiiniarvo on normaali.')
elif sukupuoli == 'NAINEN':
    if arvo < 117:
        print('Hemoglobiini arvo on alhainen.')
    elif arvo > 175:
        print('Hemoglobiiniarvo on korkea.')
    else:
        print('Hemoglobiiniarvo on normaali.')
else:
    print('Vastatkaa sukupuoleen mies/nainen.')