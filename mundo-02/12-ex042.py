r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        triangulo = 'EQUILÁTERO'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        triangulo = 'ISÓSCELES'
    else:
        triangulo = 'ESCALENO'
    print(f'As 3 retas acima formam um triângulo {triangulo}.')
else:
    print('As 3 retas acima NÃO formam um triângulo.')
