n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
cor = {
    'limpa': '\33[m',
    'branco': '\33[30m',
    'vermelho': '\33[31m',
    'verde': '\33[32m'
}
print('A soma entre {}{}{} e {}{}{} é: {}{}{}!'.format(cor['vermelho'], n1, cor['limpa'], cor['vermelho'], n2,cor['limpa'], cor['verde'], s, cor['limpa']))
