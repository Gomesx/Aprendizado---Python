n = int(input('Digite um Número Inteiro: '))

print('''Escolha uma das bases para conversão do número 
1 para escolher BINÁRIO
2 para escolher OCTAL
3 para escolher HEXADECIMAL''')

op = int(input('Sua Escolha: '))

if op == 1:
    print('{} convertido para BINÁRIO é {}'.format(n, bin(n)[2:])) # bin(n) é responssável por comverter o número
    
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(n, oct(n)[2:])) # oct(n) converte o valor em octal
    
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n, hex(n)[2:])) # hex(n) converte o valor para hexadecimal
    
else:
    print('Opção Inválida, digite novamente!')