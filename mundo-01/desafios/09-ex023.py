num = input('Digite um número: ')
num = num.rjust(4, '0')
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))

"""Forma matemática:"""

numero = int(input('Digite um número: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 100 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))