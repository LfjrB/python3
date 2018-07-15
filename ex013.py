sal = float(input('Qual o salário do funcionário? R$ '))
d = int(input('Qual a porcentagem de acréscimo? '))
f = ((sal * d) / 100) + sal

print('Um funcionário que ganhava R${:.2f}, com {}% de acréscimo, passa a receber R${:.2f}.'.format(sal, d, f))