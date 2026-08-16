distancia = int(input('Qual a distância da viagem? '))

if distancia <= 200:
    print(f'O preço da passagem será de R$ {distancia * 0.5}')
else:
    print(f'O preço da passagem será de R$ {distancia * 0.45}')