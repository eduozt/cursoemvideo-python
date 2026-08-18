nome = input('Qual é o seu nome? ')
if nome == 'Eduardo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Lucas' or nome == 'Maria':
    print('Seu nome é bem popular!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')