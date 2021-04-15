print('\033[1;32mOlá, sou a calculadora de pagamentos! Digite os dados pedidos, que eu irei calcular o preço do produto. \033[m')
print('-=-' *20)

valor = int(input('\033[1;32mDigite o valor do produto: R$ \033[m'))
print('''Escolha o seu método de pagamento
[1] à vista ou cheque;
[2] à vista no cartão;
[3] em até 2x no cartão;
[4] 3x ou mais parcelas no cartão.''')

esc = int(input('\033[1;32mEscolha o método de pagamento: '))

if esc == 1:
    des = 0.9 * valor
    print('\033[1;33mÀ vista ou cheque terá 10% de desconto, logo o valor será R${:.2f}'.format(des))
    
elif esc == 2:
    des = 0.95 * valor
    print('\033[1;34mÀ vista no cartão terá 5% de desconto, logo o valor será R${:.2f}'.format(des))
    
elif esc == 3:
    des = valor
    print('\033[1;35mEm até 2x no cartão não terá desconto, logo o valor será R${:.2f}'.format(des))
    
elif esc == 4:
    par = int(input('Quantas parcelas? '))
    aum = 1.2 * valor
    mensal = aum / par
    print('\033[1;36m3x ou mais parcelas no cartão terá o aumento de 20%, logo o valor será R${:.2f}'.format(aum))
    print('\033[1;36mCom {} parcelas, pagando R${} mensalmente'.format(par,mensal))
    
else:
    print('Escolha errada. Digite Novamente.')
    
