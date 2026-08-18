decimal = int(input('Digite um número: '))
print('-' * 25)
print('''Para qual base deseja converter?
      1 - Binário
      2 - Octal
      3 - Hexadecimal''')
base = int(input('\33[34mDigite a sua opção: '))

if base == 1:
    binario = bin(decimal)[2:]
    print(f'O número {decimal} na base binária é {binario}')
elif base == 2:
    octal = oct(decimal)[2:]
    print(f'O número {decimal} na base octal é {octal}')
elif base == 3:
    hexadecimal = hex(decimal)[2:]
    print(f'O número {decimal} na base hexadecimal é {hexadecimal}')
else:
    print('\33[31mOpção inválida')