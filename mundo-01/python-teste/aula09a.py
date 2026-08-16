"""
Manipular strings, textos
Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

strip() -> remove espaços inúteis no começo e final de uma string
rstrip() -> remove só os espaços depois - right
lstrip() -> remove os espaços antes - left
"""

frase = 'Curso em Vídeo Python'

"""print(frase[9:14])"""

print('A frase tem {} caracteres'.format(len(frase)))

print('A frase tem {} letras "o"'.format(frase.count('o', 0, 21)))

print('Encontrei "deo" começando na posição {}'.format(frase.find('deo')))

print('curso' in frase.lower())

frase = frase.replace('Python', 'Android')

frase = frase.capitalize()

frase = frase.title()

frase = frase.split(" ", 1)

print('-'.join(frase))

print("""Gostou da aula? Então torne-se um Gafanhoto APOIADOR do CursoemVídeo acessando o site
cursoemvideo.com/apoie
Aula do Curso de Python criado pelo professor Gustavo Guanabara para o portal CursoemVideo.com.""")