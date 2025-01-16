pituus = float(input('Kuinka pitkän kuhan nappasit?'))
vajaa = 37 - pituus
if pituus < 37:
    print(f'Vapauta kuha välittömästi! Minimi mitasta vajaana: {vajaa}cm.')
else:
    print('Kuha on sopivan mittainen pidettäväksi!')