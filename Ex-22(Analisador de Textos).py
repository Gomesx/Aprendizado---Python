nome = str(input('Digite o nome completo: ')).strip()  #.strip() tira os espaços desnecessários

print('Analisando o nome...')

print('O seu nome totalmente maiúsculo: {}'.format(nome.upper()))
print('Já totalemnte minúsculo: {}'.format(nome.lower()))
print('O nome possui {} letras'.format(len(nome) - nome.count(' '))) # Subtração entre o carcateres (epsçao e letras) - os espaços existentes no meio
#print('O seu primeiro nome possui {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele possui {} letras'.format(separa[0], len(separa[0])))
