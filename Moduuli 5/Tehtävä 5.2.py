luvut = []
luku = input('Anna luku tai lopeta painamalla enter:')
while luku != '':
    luku = int(luku)
    luvut.append(luku)
    luku = input('Anna seuraava luku tai lopeta painamalla enter:')
else:
    print('Luvut suuresta pienempään:')
    print(f'{luvut.sort(reverse=True)}')