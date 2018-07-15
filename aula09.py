'''nome = ' Seu Jornal Não Vende Mais. '
print(len(nome))
print(nome.count('e'))
print(nome.find('Não'))
print('jornal'in nome)
print(nome.replace('jornal','pastel'))
print(nome.upper())
print(nome.lower())
print(nome.capitalize()) #joga todos caracteres pra minúsculo deixa só a primeira letra em maiúsculo
print(nome.title()) #analisa quantas palavras tem a string (lê pela posição de espaço, onde tiver, ele faz a quebra de palavra) e transforma a inicial em maiúsculo.
print(nome.strip()) #remove espaços inúteis
print(nome.rstrip()) #right/direita remove somente os últimos espaços
print(nome.split()) #divide em uma lista
print('-'.join(nome))'''

frase = 'Curso em Vídeo Python'
print(frase[:14])
print("""O que é Lorem Ipsum?
Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.""")