print('\033[1;32mOlá, gostaria de saber a sua idade, a fim de saber quanto tempo falta para você se alistar? \033[m')
print('\033[1;32mEntão digite os seus dados abaixo. \033[m')
print('-=-' * 20)

exer = 18
idade = int(input('\033[1;32mQual a sua idade? \033[m'))
print('\033[1;32mCerto... então você possui {} anos. \033[m'.format(idade))

if idade < exer:
    t1 = exer - idade
    print('\033[1;33mAinda faltam {} ano(s) para você se alistar ao serviço militar.\033[m'.format(t1))

elif idade == exer:
    print('\033[1;33mEstá no momento de você se alistar! \033[m')

else:
    t2 = idade - exer
    print('\033[1;33mBem, o seu prazo de alistamento já passou! Você está {} ano(s) atrasado. \033[m'.format(t2))
    
print('Obrigado por dedicar seu tempo ao país!')
    