print('\33[34m' + '-=' * 30 + '-\33[m')
print('Será que essas 3 retas podem formar um triângulo?')
print('\33[34m' + '-=' * 30 + '-\33[m')

r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas acima podem formar um triângulo.')
else:
    print('As retas acima NÃO podem formar um triângulo.')