n = int(input('Digite um número e saiba se é PRIMO: '))
divisoes = 0

for c in range(1,n+1):
    if n % c == 0:
        divisoes += 1
        print(f'\33[34m{c}', end=' ')
    else:
        print(f'\33[31m{c}', end=' ')

if divisoes == 2:
    print(f'\n\33[mO número {n} foi divisível por 1 e por ele mesmo. Então é PRIMO.')
else:
    print(f'\n\33[mO número {n} foi divisível por {divisoes} números. Logo, não é PRIMO.')