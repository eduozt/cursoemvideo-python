import math
from math import radians

angulo = int(input('Digite um ângulo: '))

sen = math.sin(radians(angulo))
cos = math.cos(radians(angulo))
tg = math.tan(radians(angulo))

print('Para o ângulo {}º, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, sen, cos, tg))
