print('Quer saber quanto você obteve de aumento? Ok... Deixe comigo')

sal = float(input('Digite quanto você recebe: '))

if sal > 1250.00:
    a1 = sal * 0.10
    nsal1 = sal + a1
    print('Pois bem, você obteve um aumento de R$ {:.2f}, logo receberá R$ {:.2f}'.format(a1, nsal1))
    
else:
    a2 = sal * 0.15
    nsal2 = sal + a2
    print('Pois bem... você obteve um aumento de R$ {:.2f}, logo receberá R$ {:.2f}'.format(a2, nsal2))
    