import random
number = random.randint(1,10)
player = float(input('Arvaa luku 1-10:'))
while player != number:
    if number > player:
        print('Liian pieni arvaus')
        player = float(input('Arvaa uudestaan:'))
    elif number < player:
        print('Liian suuri arvaus')
        player = float(input('Arvaa uudestaan:'))
else:
    print('Oikein!')