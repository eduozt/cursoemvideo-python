cidade = input('Digite o nome de uma cidade: ').strip()

dividido = cidade.lower().split()

santo = 'santo' in dividido[0]

print('O nome da cidade começa com Santo? {}'.format(santo))