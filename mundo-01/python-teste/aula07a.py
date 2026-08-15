"""
Operadores Aritméticos:

+ adição
- subtração
* multiplicação
/ divisão
** potenciação
// divisão inteira
% módulo (resto da divisão)

"""

print('5 + 2 = {}'.format(5 + 2))
print('5 - 2 = {}'.format(5 - 2))
print('5 * 2 = {}'.format(5 * 2))
print('5 / 2 = {}'.format(5 / 2))
print('5 ** 2 = {}'.format(5 ** 2))
print('5 // 2 = {}'.format(5 // 2))
print('5 % 2 = {}'.format(5 % 2))


"""
Ordem de precedência:

1: ()
2: **
3: * / // %
4: + -
"""

print(5 + 3 * 2 == 16)
print((5+3) * 2 == 16)