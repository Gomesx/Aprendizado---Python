print('\033[1;33m-=-\033[m' * 20)
print('     Dez primeiros termos de uma PA     ')
print('\033[1;33m-=-\033[m' * 20)

n1 = int(input('Primeiro termo: '))
r =  int(input('Razão: '))
d = n1 +(10 - 1) * r

for c in range (n1, d + r, r):
    print('{}'.format(c), end=' -- ')
print('Acabou')
    
