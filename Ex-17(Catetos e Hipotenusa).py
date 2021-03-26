from math import sqrt,pow

catop = float(input('Digite o valor do cateto oposto do triângulo retângulo: '))
catadj = float(input('Digite o valor do cateto adjacente do triângulo retângulo: '))

n1 = pow(catop,2) + pow(catadj,2) # A resolução também poderia - n1 = math.hypot(catop,catadj)
hip = sqrt(n1)

print('Hipotenusa = {:.2f}'.format(hip))
