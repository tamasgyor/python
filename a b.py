a = 'Hello'
print(a.split(','))
b = 'World'
c = a + b
print(c)



gyumolcs = 'banán'
lista = list(enumerate(gyumolcs))
print(lista)



primek = [2,3,5,7,11,13,17,19,23,31]
p4 = primek[4]
print(p4)

gyumolcs = 'banán'
hossz = len(gyumolcs)
print(hossz)

i = 0
while i < len(gyumolcs):
    karakter = gyumolcs[i]
    print(karakter)
    i += 1

for c in gyumolcs:
    print(c)



nev = 'Alice'
kor = 10
s2 = 'A nevem {1}, és {0} éves vagyok.'.format(kor, nev)
