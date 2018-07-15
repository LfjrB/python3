larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
a = larg * alt
lit = a / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(larg, alt, a))
print('Para pintar esta parece, você precisará de {}l de tinta.'.format(lit))