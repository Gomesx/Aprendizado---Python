#from random import choice isto; ou:
from random import randint
from time import sleep
print('Vamos brincar de advinhação!')
print('-=-' * 20)
print('O computador escolheu um número, duvido você advinhar esse número!')
human = int(input('Escolha um número entre 0 e 5: '))
print('Certo... Vamos Lá!')
print('-=-' * 20)
print('Vejamos...')
sleep(1)

#n0 = 0
#n1 = 1
#n2 = 2
#n3 = 3
#n4 = 4
#n5 = 5
#lista = [n0, n1, n2, n3, n4, n5]
#pc = choice(lista)
pc = randint(0,5)

if human == pc:
    print('O computador escolheu {} e você escolheu o número {}, logo você ganhou!'.format(pc, human))
    
else:
    print('O computador escolheu {} e você escolheu o número {}, sendo assim, você perdeu!'.format(pc,human))
