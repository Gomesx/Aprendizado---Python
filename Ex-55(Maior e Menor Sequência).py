s = 0
cont = 0
tot = 0
maior = 0
menor = 0

for c in range(0,5):
    
    tot = tot + 1
    peso = float(input('Digite o peso da {}º pessoa: '.format(tot)))
    
    if peso == 1:
            maior = peso
            menor = peso
    else:
        if peso > maior:
                maior = peso
            
        if peso < menor:
                menor = peso
            
print('\nO maior peso lido foi de {}'.format(maior))
print('O menor peso lido foi de {}'.format(menor))
  