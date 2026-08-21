somaidade = 0
idadehvelho = 0
mj = 0

for c in range(1,5):
    nome = input(f'Nome {c}: ')
    idade = int(input(f'Idade {c}: '))
    sexo = input(f'Sexo {c} (masc ou fem): ').lower()
    somaidade =+ idade
    if sexo == 'masc' and idade > idadehvelho:
        idadehvelho = idade
        hvelho = nome
    if sexo == 'fem' and idade < 20:
        mj =+ 1
print(f'''A média de idade do grupo é {somaidade / 4} anos.
O homem mais velho é o {hvelho}.
E existem {mj} mulheres com menos de 20 anos.''')