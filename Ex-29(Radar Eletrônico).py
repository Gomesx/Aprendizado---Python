print('Quer saber se você foi multado? Digite a sua velocidade abaixo.')

vel = float(input('Qual foi a sua velocidade no trecho Campinas-São Paulo: '))

if vel > 80:
    dif = vel - 80
    multa = dif * 7
    print('Puts, você passou a velocidade de 80 km/h; a sua velocidade foi de {:.2f} km/h. Sendo assim, sua multa foi de R${:.2f}'.format(vel, multa))

else:
    print('Ufa... Você não ultrapassou o limite de 80 km/h.')
    
print('Tenha um bom dia. Diriga com segurança!')
    
    