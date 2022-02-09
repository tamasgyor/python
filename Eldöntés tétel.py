"""
*Egy sorozathoz egy értéket rendelő algoritmusok​
    Sorozatszámítás​
        Összegzés​
        Szorzás​
        Összefűzés​
        bool
    Eldöntés​
    Kiválasztás​
    Lineáris keresés​
    Megszámlálás​
    Maximum kiválasztás​
    Minimum kiválasztás​
*Egy sorozathoz egy sorozatot rendelő algoritmusok​
*Több sorozathoz egy sorozatot rendelő algoritmusok​
*Egy sorozathoz több sorozatot rendelő algoritmusok​
https://szit.hu/doku.php?id=oktatas:programozas:programozasi_tetelek:python_megvalositas



#Összegzés - összeadás
t = [ 3, 8, 2, 4, 5, 1, 6]
 
osszeg = 0
for num in t:
    osszeg = osszeg + num
 
print("Összeg: ", osszeg)
#print(f' összeg egyenlő {sum(t)}')


#Összegzés - szorzás
osszeg = 1
for num in t:
    osszeg = osszeg * num
 
print("Összeg: ", osszeg)

#Összegzés - konkatenáció
osszeg = ''
for num in t:
    osszeg = str(osszeg) + str(num)
 
print("Összeg: ", osszeg)


#Feladat
#A róka libát lop a faluból. A libák súlyát – pontosabban tömegét – listában adjuk meg.
#A farkas a dűlőútnál várja a rókát, és a három kilónál nagyobb libákat elveszi –
#a piciket nagylelkűen otthagyja a rókának. Hány kiló libát ehet meg a róka?
#Az előző feladat algoritmusát felhasználva írjuk meg azt az algoritmust, amelyik ezt a problémát oldja meg!

libák = [1,5,2,3,4]

rókának_jut = 0
for liba in libák:
    if liba <= 3:
        rókának_jut += liba
print('A rókának', rókának_jut, 'kilónyi liba marad.')


#Hány libát lopott a róka?

db=0
rókának_jut = 0
for liba in libák:
    if liba <= 3:
        rókának_jut += liba
        db+=1
print('A rókának', rókának_jut, 'kilónyi liba marad.')
print(len(t))
print(db)

print('hali')

#2. óra 

#Feladat
#Egy listában tároljuk, hogy egy taxis egy nap során 
hány piculát keresett az egyes fuvarjaival.
#Mennyi pénze lett összesen?
bevételek = [1,5,2,3,4]

#Megoldás
összes = 0
for bevétel in bevételek:
    #összes += bevétel #vagy:
    összes = összes + bevétel
    print('Napi bevétel:', összes, 'picula.')
    print(f'Napi bevétel: {összes} picula.')

összes = sum(bevételek)
print('Napi bevétel:', összes, 'picula.')

#Átlagosan hány piculát keres a taxisunk egy fuvarral?
bevételek = [1,5,2,3,4]
összes = 0
darab = 0
for bevétel in bevételek:
    összes += bevétel
    darab += 1
print('Az átlagos bevétel:', összes/darab, 'picula.')

összes = sum(bevételek)
darab = len(bevételek)
print('Az átlagos bevétel:', összes/darab, 'picula.')

#Megszámolás - t = [ 3, 8, 2, 4, 5, 1, 6]
count = 0
for num in t:
    if num > 5:
        count = count + 1
 
print("5-nél nagyobb: ", count)
"""
#Eldöntés - t = [ 3, 8, 2, 4, 5, 1, 6]
t = [ 3, 8, 2, 4, 5, 1, 6]
n = len(t)
#ker = int(input('Kérem adja meg a keresett számot')
ker = 5
 
i = 0
while i < n and t[i] != ker:
    i = i + 1
    #i+=1
 
if i<n:
    print("Van ilyen: ", ker)
else:
    print("Nincs ilyen elem: ", ker)

#Feladat
#Volt-e a taxisnak ma ötpiculás bevételű fuvara?

bevételek = [1,5,2,3,4]

vanilyen = False
for bevétel in bevételek:
    if bevétel == 5:
        vanilyen = True
        break
if vanilyen:
    print('Van ötpiculás bevétel.')

if 5 in bevételek:
    print('Van ötpiculás bevétel.')

#Előfordult-e olyan, hogy a róka legalább háromkilós libát lopott?
libák = [1,5,2,3,4]
vanilyen = False
for liba in libák:
    if liba >= 3:
        vanilyen = True
        break
if vanilyen:
    print('Van legalább egy háromkilós liba.')


#Előfordult-e olyan, hogy a róka kisebb libát hozott, mint az előző napon?
#Ebben a feladatban mindenképp index szerint kell bejárnunk a listát, hiszen az aktuális elemet mindig az előzőhöz kell hasonlítani.


libák = [1,5,2,3,4]
vanilyen = False
for index in range(len(libák)):
    if index > 0:
        if libák[index] < libák[index-1]:
            vanilyen = True
            break
    if vanilyen:
        print('Volt, amikor kisebb libát lopott az előző napinál.')
        
        
 #Emlékszik?
 #ugye figyelsz a -11-re a -10 helyett?!
 #for i in range(-1, -11, -1): 
  #mama  print(i**3)

#Feladat
#Töltsünk fel egy 10 elemű, egész típusú tömböt véletlenszerűen 1 és 6 közötti egész számokkal (dobókocka).
#írjuk ki a képernyőre, van-e a tömbben 6-os. El¬lenőrzésként írassuk ki a tömb elemeit is a képernyőre.

from random import randrange
rnd = []
for i in range(10):
    rnd.append(randrange(1,7))
i = 0    
while i < 10 and rnd[i] != 6:
    i += 1
if i >= 10:
    print("Nincs benne 6-os")
else:
    print("Van benne 6-os")
for i in range(10):
    print(rnd[i], end=' ')


#Feladat
#Kérjünk be a felhasználótól egy szót, és döntsük el, hogy tartalmaz-e magán-hangzót.
#Amennyiben tartalmaz, írjuk ki, hogy "Van benne magánhangzó.". Ha nincs, akkor írjuk ki, hogy "Nincs benne magánhangzó" A begépelendő szóról feltételezhetjük, hogy csak az angol ábécé kisbetűit tartalmazza.
word = input("Kérek egy szót: ")
vowels = "aeiou"
n = len(word)
i = 0    
while i < n and vowels.find(word[i]) > -1:
    i += 1
if i >= n:
    print("Nincs benne magánhangzó.")
else:
    print("Van benne magánhangzó")




#Kiválasztást - t = [ 3, 8, 2, 4, 5, 1, 6]
n = len(t)
ker = 5
 
i = 0
while t[i] != ker:
    i = i + 1
 
print("Hányadik helyen van: ", i+1)


#Szélső értékek
# Maximun kiválasztás t = [ 5, 3, 6, 2, 1 ]
 
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)

# Minumum kiválasztás t = [ 5, 3, 6, 2, 1 ]
minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)
