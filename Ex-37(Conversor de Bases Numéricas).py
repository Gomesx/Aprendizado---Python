n = int(input('Digite um N�mero Inteiro: '))

print('''Escolha uma das bases para convers�o do n�mero 
1 para escolher BIN�RIO
2 para escolher OCTAL
3 para escolher HEXADECIMAL''')

op = int(input('Sua Escolha: '))

if op == 1:
    print('{} convertido para BIN�RIO � {}'.format(n, bin(n)[2:])) # bin(n) � responss�vel por comverter o n�mero
    
elif op == 2:
    print('{} convertido para OCTAL � {}'.format(n, oct(n)[2:])) # oct(n) converte o valor em octal
    
elif op == 3:
    print('{} convertido para HEXADECIMAL � {}'.format(n, hex(n)[2:])) # hex(n) converte o valor para hexadecimal
    
else:
    print('Op��o Inv�lida, digite novamente!')