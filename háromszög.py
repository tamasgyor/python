haromszog = [3,4,5]
print(haromszog)
ker = 0
for i in haromszog:
    ker = ker+i
    print(ker)


#haromszog = [3,4,5]

"""keres = 4
a = len(haromszog)
for i in haromszog:
    if keres == haromszog[i]:
        print(i)

wr = open('haromszög.txt','w')
wr.write(f'A háromszög kerülete {str(ker)}')
wr.close()"""






max = 0
for oldal in haromszog:
    if oldal > max:
        max = oldal 
print(f'a legnagyobb oldal mérete: {max}')