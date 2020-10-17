from random import choice, randint
 
L=['самовар', 'весна', 'лето'] 
sl=choice(L)
n = randint(0, len(sl)-1)
for i in range(len(sl)):
    if i==n:
        print('?', end='')
        continue
    print(sl[i], end='')
 
while True:
    f=input('\nВведите букву: ')
    if f==sl[n]:
        print('победа')
        break
    else:
        print('Попробуйте еще')
