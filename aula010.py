'''nome = str(input('Qual é o seu nome? '))
if nome == 'Júnior':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal! :\ ')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m == 6:
    print('Você está na média.')
elif m>6:
    print('Você está acima da média!')
else:
    print('Você está reprovado!')
