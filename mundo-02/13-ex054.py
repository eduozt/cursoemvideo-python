from datetime import date
maior= 0
anoatual = date.today().year
for c in range(1,8):
    nasc = int(input(f'Digite o ano de nascimento da pessoa {c}: '))
    if anoatual - nasc >= 21:
        maior = maior + 1
menor = 7 - maior
print(f'{menor} pessoas ainda não atingiram a maior idade e {maior} já são maiores.')