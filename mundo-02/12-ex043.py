peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / altura ** 2

if imc < 18.5:
    status = 'Abaixo do peso'
elif imc < 25:
    status = 'Peso ideal'
elif imc < 30:
    status = 'Sobrepeso'
elif imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade mórbida'
print(f'IMC: {imc}')
print(f'Status: {status}')