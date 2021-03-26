print('Quer saber se um número é par ou ímpar? Use este programa!')
n = int(input('Digite o número: '))
        
n1 = n % 2 

if n1 == 0:
    print('O número {} é par!'.format(n))

else:
    print('O número {} é ímpar'.format(n))