import random
def noppa(tahkot):
    heitto = random.randint(1,tahkot)
    print(f'Nopan arvo on:{heitto}')
    return heitto
sides = int(input('Anna tahkojen määrä:'))
while True:
    numero1 = noppa(sides)
    if numero1 == sides:
        break