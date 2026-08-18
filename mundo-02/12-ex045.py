from random import choice

opcoes = ['pedra', 'papel', 'tesoura']
computador = choice(opcoes)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))

if jogador < 0 or jogador > 2:
    print('\33[31mOpção inválida! Tente novamente.')
else:
    jogador = opcoes[jogador]

    if jogador == computador:
        resultado = 'Empate'
    elif jogador == 'pedra' and computador == 'tesoura' or jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel':
        resultado = 'Jogador venceu!'
    else:
        resultado = 'Computador venceu!'

    print(f'''Computador jogou {computador.upper()}
Jogador jogou {jogador.upper()}
{' RESULTADO ':-^30}
\33[34m{resultado:^30}\33[m
{'-'*30}''')