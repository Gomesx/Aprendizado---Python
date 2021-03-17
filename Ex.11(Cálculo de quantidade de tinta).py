print('Olá, quer saber a área e quantos litros de tinta você vai utilizar para pintar a parede? Se sim, digite o os valores abaixo.')

l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))

lata = 2
area = l * h
qdetinta = area / lata

print('Área da parede = {:.2f}'.format(area))
print('Quantidade de latas de tinta = {:.2f}'.format(qdetinta))
