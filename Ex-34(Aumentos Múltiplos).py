print('Quer saber quanto voc� obteve de aumento? Ok... Deixe comigo')

sal = float(input('Digite quanto voc� recebe: '))

if sal > 1250.00:
    a1 = sal * 0.10
    nsal1 = sal + a1
    print('Pois bem, voc� obteve um aumento de R$ {:.2f}, logo receber� R$ {:.2f}'.format(a1, nsal1))
    
else:
    a2 = sal * 0.15
    nsal2 = sal + a2
    print('Pois bem... voc� obteve um aumento de R$ {:.2f}, logo receber� R$ {:.2f}'.format(a2, nsal2))
    