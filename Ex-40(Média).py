print('Olá, irei te ajudar para saber se você foi aprovado ou não.')
print('-' * 60)

nt1 = float(input('\033[1;36mPara começar, digite a sua primeira nota: \033[m'))
nt2 = float(input('\033[1;36mDigite a sua segunda nota: \033[m'))

media = (nt1 + nt2)/2

if media < 5:
    print('\033[1;31mVocê está reprovado. \033[m')
    
elif 5 <= media <= 6.9:
    print('\033[1;33mVocê está de recuperação. \033[m')

else:
    print('\033[1;32mVocê foi aprovado. \033[m')
    

    