ano = int(input('\033[1;31mDigite o ano de nascimento do atleta pra saber a sua categoria: \033[m'))
anovig = 2021
cat = anovig - ano

if cat <= 9:
    print('Certo, o (a) atleta possui {} anos'.format(cat))
    print('\033[1;34mLogo o(a) atleta pertence a categoria MIRIM. \033[m')

elif 9 < cat <= 14:
    print('Certo, o (a) atleta possui {} anos'.format(cat))
    print('\033[1;34mLogo o(a) atleta pertence a categoria INFANTIL. \033[m')

elif 14 < cat <= 19:
    print('Certo, o (a) atleta possui {} anos'.format(cat))
    print('\033[1;34mLogo o(a) atleta pertence a categoria JUNIOR. \033[m')
    
elif 19 < cat <= 20:
    print('Certo, o (a) atleta possui {} anos'.format(cat))
    print('\033[1;34mLogo o(a) atleta pertence a cetegoria SÊNIOR. \033[m')
    
else:
    print('Certo, o (a) atleta possui {} anos'.format(cat))
    print('\033[1;34mLogo o(a) atleta pertence a cetegoria MASTER. \033[m')
    
print('Espero que tenha ajudado!')