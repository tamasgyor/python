honap= ['január','Február', 'Március','Április','Május']
for i in honap:
    print(i, end= '')
print('\na tömnb mérete:' , len(honap))
for j in range(len(honap)):
    print('%d. honap: %s' % (j+1,honap[j]))




strl = 'isz'
hb = ''
hb = 'h' + strl + 'ed'
print(hb)
print(hb[3])
hb[0] = 'v' 

strl = 'hiszed'
print(len(strl))
print(strl[1:4])
strl = strl[1:]
print(strl)
strl = strl[:3]+'o'+strl[4:]
print(strl)
