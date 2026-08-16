from random import randint
from time import sleep

escolhido = randint(0,5)

print('Pensei em um número, você consegue adivinhar?')
numero = int(input('Digite um número: '))

print('PROCESSANDO...')
sleep(2)

if escolhido == numero:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou!')

print(f'O número escolhido foi {escolhido} e você digitou {numero}.')