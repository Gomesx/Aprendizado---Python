n = int(input('''\033[1;32mEscolha 1 para iniciar o programa. 
Escolha 2 para sair do programa. 
Digite: \033[m'''))
           
s = 0            
cont = 0
if n == 1:
    
    for c in range(1,501, 2):
        resto = c % 3
    
        if resto == 0:
            cont = cont + 1
            s = s + c
        
    print('A soma dos {} números ímpares e múltiplos de três no intervalo de 1 a 500 é: {}'.format(cont, s))

if n == 2:
    print('Ok, perdão pelo incômodo.')