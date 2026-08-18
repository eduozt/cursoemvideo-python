destaque = '\33[35m'
limpa = '\33[m'

print(destaque + 'Comparador de números:' + limpa)
print('-' * 22)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'{destaque}O primeiro valor é maior.{limpa}')
elif n2 > n1:
    print(f'{destaque}O segundo valor é maior{limpa}')
else:
    print(f'{destaque}Não existe valor maior,{limpa} \33[32mos dois são iguais.')