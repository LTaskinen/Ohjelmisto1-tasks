number1 = input('Anna luku:')
suurin = None
pienin = None
while number1 !='':
    print(number1)
    if suurin == None or pienin == None:
        suurin = number1
        pienin = number1
    else:
        if number1 > suurin:
            suurin = number1
        elif number1 < pienin:
            pienin = number1
    number1 = input('Anna luku:')
else:
    print(f"Pienin luku on:{pienin} ja suurin on: {suurin}.")


