s = 0
cont = 0
for c in range(0,6):
    n = int(input('\033[1;32mDigite um número inteiro: \033[m'))
    p = n % 2
    if p == 0:
        s = s + n
        cont = cont + 1
        
print('\033[1;34mSoma dos {} valores pares é {}\033[m'.format(cont, s))

        
    
