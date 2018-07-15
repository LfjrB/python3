'''ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = ((ca ** 2) + (co **2)) ** (1/2)

print('A hipotenusa mede: {:.2f}'.format(h))'''

import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(co, ca)

print('O valor da hipotenusa é: {:.2f}'.format(h))


