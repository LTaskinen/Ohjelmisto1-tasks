luku1 = int(input('Syötä kokonaisluku:'))
if luku1 <= 1:
    print('Luku ei ole alkuluku')
else:
    for luku in range(2,int(luku1 ** 0.5),+1):
        if luku1 % luku == 0:
            print('Luku ei ole alkuluku')
        else:
            print('Luku on alkuluku')