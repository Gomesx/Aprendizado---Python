n1 = float(input('\033[1;34m Digite o primeiro número: \033[m'))
n2 = float(input('\033[1;34m Digite o segundo número: \033[m'))
print('-=-' *20)

if n1 > n2:
    print('\033[1;31m O PRIMEIRO valor é maior que o segundo valor! \033[m')
    
elif n1 < n2:
    print('\033[1;31m O SEGUNDO valor é maior que o primeiro valor! \033[m')
    
elif n1 == n2:
    print ('\033[1;31m Os dois valores são IGUAIS! \033[m')
    
print('\033[1;34m Creio que sua dúvida foi sanada :) \033[m')