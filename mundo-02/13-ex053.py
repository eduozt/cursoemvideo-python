frase = input('Digite uma frase: ')
f = frase.replace(' ','').lower()
frasenova = ''
for c in range(len(f),0,-1):
    frasenova = frasenova + f[c-1]
if f == frasenova:
    print('Essa frase é um palíndromo!')
else:
    print('Não é palíndromo.')