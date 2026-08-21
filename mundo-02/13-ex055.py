maior = 0
menor = 99999999
for c in range(1,6):
    peso = float(input(f'Digite o peso da pessoa {c}: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso informado foi {maior}Kg e o menor foi {menor}Kg.')