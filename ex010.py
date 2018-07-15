din = float(input('Quanto dinheiro você tem na carteira? R$ '))
d = din / 3.7
e = din / 4.40474

print('Com R${:.2f} você pode comprar {:.2f}$ e {:.2f} EUR.'.format(din, d, e))
