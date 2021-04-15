from time import sleep

print('Olá, vamos fazer a contagem regressiva?')

esc = int(input('''\033[1;32mEscolha [1] para iniciar a contagem regressiva.
Escolha [2] para sair do programa de contagem regressiva.
Sua Escolha: \033[m'''))


if esc == 1:
    for c in range(10, 0, -1):
        print('\033[1;36m{}\033[m'.format(c))
        sleep(1)
    print('\033[1;34mFELIZ ANO NOVO!\033[m')
        
if esc == 2:
    print('\033[1;31mOk, programa encerrado.\033[m')
    
print('Boas festas!')
