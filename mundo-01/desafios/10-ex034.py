salario = float(input('Digite o seu salário: R$ '))

if salario > 1250:
    print(f'Seu novo salário é R$ {salario * 1.1:.2f}')
else:
    print(f'Seu novo salário é R$ {salario * 1.15:.2f}')