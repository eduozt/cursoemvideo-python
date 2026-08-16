nome = input('Digite seu nome completo: ').strip()

print('Maiúsculo: {}'.format(nome.upper()))

print('Minúsculo: {}'.format(nome.lower()))

print('Qtde de letras (sem espaços): {}'.format(len(nome.replace(' ', ''))))
""" Forma que o Guanabara fez:
len(nome) - nome.count(' ')
"""
print('Qtde de letras no primeiro nome: {}'.format(len(nome.split()[0])))
