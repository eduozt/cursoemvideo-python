from random import choice

opcoes = ['pedra', 'papel', 'tesoura']
opmaquina = choice(opcoes)

resp = input('Pedra, papel ou tesoura? ').lower()

if resp == opmaquina:
    resultado = 'Empate'
elif (resp == 'pedra' and opmaquina == 'tesoura') or (resp == 'papel' and opmaquina == 'pedra') or (resp == 'tesoura' and opmaquina == 'papel'):
    resultado = 'Você ganhou!'
else:
    resultado = 'Eu ganhei! Humano fraco!'

print(f'''Máquina: {opmaquina}
Usuário: {resp}
{'-'*50}
Resultado: {resultado}
''')