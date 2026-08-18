from datetime import date
print('Descubra a sua categoria!')
print('-' * 30)
nasc = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'\33[34mA sua categoria é: {categoria}')
