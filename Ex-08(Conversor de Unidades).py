print('Olá, precisa de ajuda na conversão de valores? Se sim, digite o valor em metros abaixo')

m = float(input('Digite o valor: '))

cm = m * 100
mm = m * 1000

print('Aqui está a sua conversão...')
print('{} metros = {} centímetros'.format(m,cm))
print('{} metros = {} milímetros'.format(m,mm))
