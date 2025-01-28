luvut = []
luku = input('Anna luku tai lopeta painamalla enter:')
while luku != '':
    luku = int(luku)
    luvut.append(luku)
    luku = input('Anna seuraava luku tai lopeta painamalla enter:')
else:
    luvut.sort(reverse=True)
    print('Luvut suuresta pienempään:')
    print(luvut)