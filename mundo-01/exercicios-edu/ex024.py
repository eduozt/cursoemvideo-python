cidade = input('Digite o nome de uma cidade: ')

cidade = cidade.lower()

dividido = cidade.split()

santo = 'santo' in dividido[0]

print('O nome da cidade começa com Santo? {}'.format(santo))