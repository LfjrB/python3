d = int(input('Quantos dias? '))
km = float(input('Quantos km foram rodados? '))
pago = (d * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}!'.format(pago))
