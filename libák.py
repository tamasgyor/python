libák = [1,5,2,3,4]
vanilyen = False
for index in range(len(libák)):
    if index > 0:
        if libák[index] < libák[index-1]:
            vanilyen = True
            break
    if vanilyen:
        print('Volt, amikor kisebb libát lopott az előző napinál.')
wr = open('liba.txt','w')
wr.write
wr.close