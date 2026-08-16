dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quandos km foram rodados? '))
preco = (dias * 60) + (km * 0.15)
print('O preço a pagar é de R$ {:.2f}'.format(preco))
