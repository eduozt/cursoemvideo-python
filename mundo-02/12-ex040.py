n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print('\33[32mParabéns, você foi aprovado!')
elif 7 > media >= 5:
    print('\33[33mVocê ficou de recuperação.')
else:
    print('\33[31mVocê foi reprovado!')