num = int(input('Digite um número: '))
cont = 0

for c in range(1, num + 1):
    
    if num % c == 0:
        print('\033[1;32m', end=' ')
        cont = cont + 1
        
    else:
        print('\033[1;31m', end=' ')
    
    print('{}'.format(c), end=' ')
    
print('\n\033[mO número {} é divisível por {} números.'.format(num, cont), end=' ')
    
if cont == 2:
    print('Logo, o número {} é primo.'.format(num))
    
else:
    print('Logo, o número {} não é primo.'.format(num))