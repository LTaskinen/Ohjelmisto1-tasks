vajat = ('talvi','kevät','kesä','syksy')
kknro = int(input('Anna kuukauden numero (1-12):'))
kk = int((kknro % 12)//3)
vaika = vajat[kk]
print(f'{kknro}. kuukausi on {vaika} vuodenajassa')