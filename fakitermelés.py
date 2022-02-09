import random

wr = open('fa.txt','w')
fa = []

for x in range(30):
    x = random.randint(50,100)
    fa.append(x)
    wr.write(str(x))
    wr.write("\n")

fák = 0
for num in fa:
    fák = fák + num
print(f'Összes fa: ', {fák})

összes = 0
darab = 0
for fák in fa:
    összes += fák
    darab += 1
print(f'Az átlag:', {összes/darab}, 'fa')


maxElem = fa[0]
for elem in fa:
    if elem > maxElem:
        maxElem = elem
print(f'legnagyobb:{maxElem}')

n = len(fa)
ker = 40
i = 0
while i < n and fa[i] != ker:
    i = i + 1
if i<n:
    print(f'Van ilyen nap: ', ker)
else:
    print(f'Nincs ilyen elem: ', ker)




minElem = fa[0]
for elem in fa:
    if elem < minElem:
        minElem = elem
print(f'legnagyobb:{minElem}')






wr.write(f' Összes fa:{fák},\nAz átlag:{összes/darab},\nlegnagyobb:{maxElem},\nlegkisebb:{minElem}')

wr.close