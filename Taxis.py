bevetelek = [1,5,2,3,4,]

összes = 0
for bevetelek in bevetelek:
    összes = összes + bevetel
    print('Napi bevétel:',összes,'picula.')
    print(f'Napi bevetel: {összes} picula.')
összes = sum(bevetelek)
print('Napi bevetel:',összes,'picula.')

bevetelek =  [1,5,2,3,4]
összes = 0
darab = 0
for bevetel in bevetelek:
    összes += bevetel
    darab += 1
print('Az átlagos bevetel:',összes/darab,'picula.')

