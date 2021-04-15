from time import sleep

print('\033[1;34mOlá, quer financiar uma casa? Pois bem, digite os valores abaixo \033[m') #A letra está azul
print('-=-' * 20)

vlc = float(input('\033[1;34mQuanto custa a casa: R$ \033[m'))
s = float(input('\033[1;34mQual o valor do seu salário: R$  \033[m'))
a = float(input('\033[1;34mEm quanto anos você pretende pagar a casa?  \033[m'))

print('Certo, calculando...')
sleep(2)

meses = a * 12
mensalidade = vlc / meses
des30 = s * (30/100)

if mensalidade > des30:
    print('\033[1;31mA mensalidade excede 30% do seu salário. Você pagaria R${:.3f} mensalmente, logo o empréstimo foi NEGADO \033[m'.format(mensalidade))
    
elif mensalidade < des30:
    print('\033[1;32mA mensalidade não excedeu 30% do seu salário. Você pagará R${:.3f} mensalmente, logo o empréstimo foi APROVADO \033[m'.format(mensalidade))
    
print('\033[1;34mEspero que eu tenha ajudado \033[m')
