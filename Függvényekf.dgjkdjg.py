def aláhúzás(jel):
    for _ in range(10):
        print(jel,end='')
    print('')

print('Ez egy fontos figyelmeztetés!')
aláhúzás('-')
print('Minden sora nagyon fontos!')
aláhúzás('*')
print('Komolyan!')
aláhúzás('~')

def pluszkettő(szám):
    print(szám+2)

print('5+2= ', end='')
pluszkettő(5)
print('4+2= ', end='')
pluszkettő(4)

def pluszkettő(szám):
    return szám+2

print('5+2=', pluszkettő(5))
print('4+2=', pluszkettő(4))

def megítél(mondat):
    if len(mondat) > 0:
        if mondat[-1] != '!' and mondat[-1] != '?' and mondat[-1] != '.':
            print('Hát enyje!')
        else:
            print('Igazán gyönyörű mondat!')

#mondat = None
#while mondat != '':
 #   mondat = input('Írj be egy mondatot!')
 #   megítél(mondat)


def pozneg(szám):
    if szám > 0:
        print(szám, 'pozitív.')
    elif szám < 0:
        print(szám, 'negatív.')
    else:
        print('A szám nulla.')

szám = None
while szám != '':
    szám = input('Írj ide egy számot!')
    if szám != '':
        szám = float(szám)
        pozneg(szám)