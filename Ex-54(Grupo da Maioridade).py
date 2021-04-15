tot = 0
cont = 0 
n = 0
av = 2021

for c in range(0,7):
    
    tot = tot + 1
    ano = int(input('\033[1;32mDigite o ano de nascimento da {}º pessoa: \033[m'.format(tot)))
    m = av - ano 
    if m >= 18:
        cont = cont + 1
        menor = 7 - cont
        
print('''\nDo grupo de 7 pessoas: {} são maiores de idade. Assim, {} são menores de idade'''.format(cont,menor))
