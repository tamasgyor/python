
t = [3,8,2,4,5,1,6]
összes = 0
for összes in t:
    összes = összes + t
    print(f'ennyi: {összes}')
összes = sum(bev)
print('Napi bevétel:', összes, 'picula.')



n = len(t)
count = 0
for num in t:
    if num > 5:
        count = count + 1
print('5-nél nagyobb: ', count)


