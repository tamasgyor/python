eletkor = int(input('Mi az életkora ?'))
nev = input('Mi a neve ?')
if eletkor <= 3:
    print('totyogó')
elif eletkor <= 6:
    print('Hackeljük meg az óvodát!')
elif eletkor <= 14:
    print('Felhőtechnológia a menzán')
elif eletkor <= 18:
    print('Big data a középiskolában')
print(f'{nev},{eletkor}')