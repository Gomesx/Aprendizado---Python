print('Olรก, irei calcular o seu imc :) !')
print('-=-' * 20)

massa = float(input('\033[1;34mPrimeiro, digite a sua massa em kg: \033[m'))
altura = float(input('\033[1;34mSegundo, digite a sua altura em metros(Coloque assim, por exemplo, 1.89): \033[m'))

imc = massa/(altura * altura)

if imc < 18.5:
    print('\033[1;35mIMC = {:.1f} \033[m'.format(imc))
    print('\033[1;31mAbaixo do peso! \033[m')
    
elif 18.5 < imc <= 25:
    print('\033[1;35mIMC = {:.1f} \033[m'.format(imc))
    print('\033[1;32mPeso ideal. \033[m')
    
elif 25 < imc <= 30:
    print('\033[1;35mIMC = {:.1f} \033[m'.format(imc))
    print('\033[1;33mSobrepeso! \033[m')

elif 30 < imc <= 40:
    print('\033[1;35mIMC = {:.1f} \033[m'.format(imc))
    print('\033[1;33mObesidade! \033[m')

else:
    print('\033[1;35mIMC = {:.1f} \033[m'.format(imc))
    print('\033[1;31mObesidade Mórbida! \033[m')
    
print('Espero ter sido útil.')