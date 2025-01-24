import random
nopat = int(input('Montako noppaa heitetään?'))
summa = [random.randint(1,6) for _ in range(nopat)]
print(f'Noppien luvut:{summa}')
print(f'Noppien summa on: {sum(summa)}')