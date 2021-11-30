import random

nev = input('Kérem adja meg a nevét')
szam1 = float(input('adja meg egy számot'))
szam2 = random.randrange(10,50)
SZAM3 = 5
szamok2 = {23}
szamok2.add(szam1)
szamok2.add(szam2)
szamok2.add(SZAM3)

wr = open('Tamás.txt','w')
wr.write(nev)
wr.close()
my_list=[1,2,3,4,5,'abc,''def']
with open('your_file.txt','w') as file:
    for item in my_list
        file.write('%\n' % item)
