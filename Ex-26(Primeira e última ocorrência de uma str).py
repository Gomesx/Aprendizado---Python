f = str(input('Qual a frase desejada? ')).upper().strip()
a = str('a')

print('Analisando o nome...')
print('A letra {} aparece {} vezes na frase'.format(a, f.count('A')))
print('A letra {} aparece pela 1º vez na posição {}'.format(a, f.find('A') + 1 ))
print('A letra {} aparece pela última vez na posção {}'.format(a, f.rfind('A') + 1))