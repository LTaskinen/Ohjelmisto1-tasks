import random
def noppa():
    heitto = random.randint(1,6)
    print(f'Nopan arvo on:{heitto}')
    return heitto
while True:
    numero1 = noppa()
    if numero1 == 6:
        break