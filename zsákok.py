from tkinter import N


zsak = [2,9,19,20,5,7]
osszeg = 0
for num in zsak:
    osszeg = osszeg + num
print(f'Össztömeg: ', {osszeg})
 
összes = 0
darab = 0
for bevétel in zsak:
    összes += bevétel
    darab += 1
print(f'Az átlag:', {összes/darab}, 'kg')




n = len(zsak)
count = 0
for num in zsak:
    if num == 5:
        count = count +1
print(f'Ennyi 5kg-os van: {count}')


maxElem = zsak[0]
for elem in zsak:
    if elem > maxElem:
        maxElem = elem
print(f'legnagyobb:{maxElem}')

minElem = zsak[0]
for elem in zsak:
    if elem < minElem:
        Elem = elem
print(f'legkisebb:{minElem}')


wr = open('zsak.txt','w')
wr.write(f' Össztömeg:{osszeg},\nAz átlag:{összes/darab},\nEnnyi 5kg-os van:{count},\nlegnagyobb:{maxElem},\nlegkisebb:{minElem}')
wr.close()