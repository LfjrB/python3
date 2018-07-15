import math
a = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(a))
print('O ângulo {} tem o SENO de {:.2f}'.format(a, seno))
cosseno = math.cos(math.radians(a))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(a, cosseno))
tan = math.tan(math.radians(a))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(a, tan))

