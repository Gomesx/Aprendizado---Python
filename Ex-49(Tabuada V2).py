n = int(input('\033[1;32mDigite um n�mero inteiro para saber sua tabuada: \033[m'))

for c in range(1, 11):
    m = n * c
    print('{} x {} = {}'.format(n, c, m)) # m tamb�m podia ser n*c
    
print('\033[1;32mEspero que tenha sido �til :)!\033[m')