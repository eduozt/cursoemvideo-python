nome = input('Digite seu nome completo: ').strip()

print('O primeiro nome é: {}'.format(nome.split()[0]))
"""print('O último nome é: {}'.format(nome.rsplit(' ', 1)[1]))"""
print('O último nome é: {}'.format(nome.split()[-1]))
