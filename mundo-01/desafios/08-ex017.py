"""
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa desse triângulo retângulo é igual a {}'.format(h))
"""

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa mede: {:.2f}'.format(hypot(co, ca)))