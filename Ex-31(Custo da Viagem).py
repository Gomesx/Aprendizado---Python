from time import sleep
print('Olá, sou a calculadora de viagens!')

dist = float(input('Digite a distância que você irá viajar: '))
print('Certo, calculando...')
sleep(1)

if dist <= 200:
    valor1 = dist * 0.50
    print('A sua viagem de {:.2f} km custará R$ {:.2f}'.format(dist, valor1))
    
else:
    valor2 = dist * 0.45
    print('A sua viagem de {:.2f} km custará R$ {:.2f}'.format(dist,valor2))
    