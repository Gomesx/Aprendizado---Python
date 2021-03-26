from random import choice # Pode ser "import random"

a1 = str(input('Qual o nome do primeiro aluno: '))
a2 = str(input('Qual o nome do segundo aluno: '))
a3 = str(input('Qual o nome do terceiro aluno: '))
a4 = str(input('Qual o nome do quarto aluno: '))
lista = [a1, a2, a3, a4] # Lista de Elementos = []

aluno = choice(lista) # Pode ser random.choice

print('O aluno escolhido para apagar o quadro foi {}'.format(aluno))
               
