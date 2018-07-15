'''km = float(input('Distância em km: '))
if km < 200:
    print('Sua passagem custará R${:.2f}.'.format(km * 0.5))
else:
    print('Viagem mais longa. Sua passagem custará R${:.2f}.'.format(km * 0.45))'''

'''d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
'''


d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f} Km.'.format(d))
preço = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

