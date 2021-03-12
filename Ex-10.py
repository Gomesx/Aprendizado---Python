print('Seja bem-vindo ao convertor de moedas!')

valore = float(input('Por favor, digite quantos reais você possui: '))
valord = valore / 5.53 # Cotação do dolár 11/03/2021

print(' O valor em doláres é de ${:.2f}'.format(valord))