import sys
oldout = sys.stdout
print('Képernyőre ír.')
wr = open('test2.txt','w')
sys.stdout = wr
print('Fájlba ír.')
wr.close()
sys.stdout = oldout
print('Képernyőre ír ismét.')