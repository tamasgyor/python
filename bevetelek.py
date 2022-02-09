bevetelek = [3,8,10,19.35,-6,5.1,9,20]

vasarolt_a_pincer = False

for bevetel in bevetelek:
    if bevetel < 0:
        vasarolt_a_pincer = True
        break

if vasarolt_a_pincer:
    print(f'a pincér vásárolt')
else:
    print(f'a pincérnek fizettek')

n = len(bevetelek)
print(n)
print(f'bevetel sum(bevetel)')

wr = open('pincér.txt','w')
for i in bevetelek:
    wr.write(f'{i}\n')
    




wr.close()