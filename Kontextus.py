with open('10b.txt','w',encoding = 'utf8') as file:
    file.write('10B')


with open('10b.txt','r',encoding = 'utf8'):
    wr = open('10b.txt','a')
    wr.write('SZBJ')
    wr.close