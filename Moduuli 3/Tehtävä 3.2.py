roomid = input('Antakaa hyttiluokkanne:').upper()
if roomid == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif roomid == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif roomid == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif roomid == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka')
