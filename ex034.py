sal = float(input('Digite um valor correspondente ao salário mensal do funcionário: '))
desc = (sal*10)/100 if sal > 1250 else (sal*15)/100
print('O salário de R${} com o reajuste ficará R${} reais.'.format(sal, desc+sal))

