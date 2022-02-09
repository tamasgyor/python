def nev(n):
    if n != 0:
        nev(n-1)
        print('Tamás')
nev(100)


def akóba_vált(liter):
    return liter/58.6

print('999 liter az', akóba_vált(999),'akó')



def betűkkel(szám):
    számok_nevei = ['nulla','egy','kettő','három','négy','öt','hat','hét','nyolc','kilenc']
    return számok_nevei[szám]

for szám in range(10):
    print(szám,betűkkel(szám))