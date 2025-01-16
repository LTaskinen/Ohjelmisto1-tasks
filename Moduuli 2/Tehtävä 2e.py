Leiviska = float(input('Anna leiviskät:'))
Naulat = float(input('Anna naulat:'))
Luodit = float(input('Anna luodit:'))
Luotisum = Luodit * 0.0133
Naulasum = Naulat * 32 * 0.0133
Leiviskasum = Leiviska * 20 * 32 * 0.0133
paino = Luotisum + Naulasum + Leiviskasum
grammat = paino%1 * 1000
print(f'Massa nykymitoin:')
print(f'{int(paino)}Kg ja {grammat:.2f}g')