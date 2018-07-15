p = float(input('Qual o valor do produto? '))
d = int(input('Qual a porcentagem de desconto? '))
f = (d * p) / 100
fin = p - f
print('O produto que custava {}, na promoção com desconto de {}% vai custar {:.2f}'.format(p, d, fin))
