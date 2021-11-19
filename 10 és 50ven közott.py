import random

szam = random.randrange(0,50)
szam2 = random.randrange(10)
lista1 = [szam,szam2]
lista2 = []
while szam2>szam:
    szam = random.randrange(0,50)
for i in lista1:
    print(i)
print('for ciklus')
print(szam)
print(szam2)
if szam < szam2:
    print(szam/szam2)
    print(szam//szam2)
    print(szam%szam2)
else:
    a1 = (szam2/szam)
    b2 = (szam2//szam)
    c3 = (szam%szam)

lista2.append(a1)
lista2.append(b2)
lista2.append(c3)
lista2.sort()
print(lista2)
