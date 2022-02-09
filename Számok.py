szam1 = int(input('Kérem adjon meg egy számot!'))
def pozneg(szam1):
    if szam1 > 0:
        print(szam1,'pozitív')
    elif szam1 < 0:
        print(szam1,'negatív')
    else:
        print('A szám nulla.')
wr = open('GyT','w')
wr.write('valami')
wr.close()
while szam1 !='':
    szam1 = input('Írj ide egy számot')
    if szam1 != '':
        szam1 = float(szam1)
    pozneg(szam1)

