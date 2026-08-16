frase = input('Digite uma frase: ')

frase = frase.lower()

print('A letra A aparece {} vezes.'.format(frase.count('a')))

print('Ela aparece a primeira vez na posição {}'.format(frase.find('a')))

print('E aparece a última vez na posição {}'.format(frase.rfind('a')))