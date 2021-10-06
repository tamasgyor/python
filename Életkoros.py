eletkor = int(input('Mi az életkora ?'))
if eletkor <= 13:
    print('GYermek')
elif eletkor <= 17:
    print('Fiatalkorú')
elif eletkor <= 23:
    print('Ifjú')
elif eletkor <= 59:
    print('Felnőtt')
else:
    print('Idős')
