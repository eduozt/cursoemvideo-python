from unidecode import unidecode

frase = input('Digite uma frase: ').strip().lower()

frase = unidecode(frase)

print(frase)

print('A letra A aparece {} vezes.'.format(frase.count('a')))

print('Ela aparece a primeira vez na posição {}'.format(frase.find('a') + 1))

print('E aparece a última vez na posição {}'.format(frase.rfind('a') + 1))