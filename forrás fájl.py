forrásfájl = open('raspberries.txt','w', encoding='utf-8')
rpik = []
for sor in forrásfájl:
    rpik.append(sor.strip().split(','))
forrásfájl.close()