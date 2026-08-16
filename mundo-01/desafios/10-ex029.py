velocidade = int(input('Digite a velocidade do carro em Km/h: '))

if velocidade > 80:
    print(f'Você foi multado pois está {velocidade - 80}Km/h acima da velocidade permitida!')
    print(f'Valor da multa: R$ {(velocidade - 80) * 7:.2f}')
