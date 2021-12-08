import random

nev = input('Kérem adja meg a nevét')
szam1 = float(input('adja meg egy számot'))
szam2 = random.randrange(10,50)
SZAM3 = 5
while szam2%2 == 1:
    szam2 = random.randint(10,50)
print(szam1)
print(szam2)
print(SZAM3)

szamok = []
szamok.append(szam1)
szamok.append(szam2)
szamok.append(SZAM3)
print(szamok)


wr = open('Tamás404.txt','w')
wr.write('Oksi')
wr.close

'''import codecs

wr = codecs.open('Tamás404.txt','a',encoding = 'utf8')
wr.write('Szeretem a pythont!!!!!')
print(wr)
wr.close
'''
f = open('Tamás404.txt','r')
tartalom = f.read()
print(tartalom)
f.close

