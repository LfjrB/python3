vel = int(input('Velocidade: '))
l = 80
if vel > 80:
    print('MULTADO! Você excedeu o limite  permitido que é 80 km/h. Limite marcado: {}km/h.'.format(vel))
    m = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia. Dirija com cuidado!')
