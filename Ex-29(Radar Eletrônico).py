print('Quer saber se voc� foi multado? Digite a sua velocidade abaixo.')

vel = float(input('Qual foi a sua velocidade no trecho Campinas-S�o Paulo: '))

if vel > 80:
    dif = vel - 80
    multa = dif * 7
    print('Puts, voc� passou a velocidade de 80 km/h; a sua velocidade foi de {:.2f} km/h. Sendo assim, sua multa foi de R${:.2f}'.format(vel, multa))

else:
    print('Ufa... Voc� n�o ultrapassou o limite de 80 km/h.')
    
print('Tenha um bom dia. Diriga com seguran�a!')
    
    