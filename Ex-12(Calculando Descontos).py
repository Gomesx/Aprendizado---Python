print('Seja bem vindo ao desconta tudo!')

p0 = float(input('Digite o preço do produto sem desconto: R$' ))

p1 = p0 * (5/100)
p2 = p0 - p1

print('O seu desconto será de R${:.2f}. Logo, o valor final do produto será R${:.2f}'.format(p1,p2))

