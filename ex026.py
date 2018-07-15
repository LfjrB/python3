fr = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes.'.format(fr.count('A')))
print('A letra A aparece na posição {} pela primeira vez.'.format(fr.find('A')+1))
print('A letra A aparece na posição {} pela ultima vez.'.format(fr.rfind('A')+1))
