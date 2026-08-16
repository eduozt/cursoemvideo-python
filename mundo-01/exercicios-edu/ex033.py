n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

#Verificar maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#Verificar menor
menor = n1
if n2 < n1 and n2 < n3:
    menor =n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

"""print(f'O maior número é {max(n1, n2, n3)}')
print(f'O menor número é {min(n1, n2, n3)}')"""