from math import radians, sin, cos, tan

angulo = int(input('Digite um ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Para o ângulo {}º, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))
