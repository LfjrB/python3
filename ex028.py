from random import randint
from time import sleep
n = randint(0, 5) #faz o comp pensar em um número aleatório
p = int(input('Hmmm... Vou pensar um número, se prepare para chutar: '))
print('-=-' * 11)
if p == n:
    print('Parabéns, você acertou!')
else:
    print('Você errou! O número chutado foi {}, mas eu pensei em {}.'.format(p, n))
print('-=-' * 11)
