n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
print('A soma vale {}, \n o produto é {} e \n a divisão é {:.3f}'.format(s, m, d), end=' --- ')
print('A potência é {}'.format(p))
