co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa desse triângulo retângulo é igual a {}'.format(h))
