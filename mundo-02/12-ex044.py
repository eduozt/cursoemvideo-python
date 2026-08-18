preco = float(input('Digite o preço do produto: R$ '))
print('''\33[34mFormas de pagamento\33[m:
    1 - À vista dinheiro/cheque: 10% de desconto
    2 - À vista no cartão: 5% de desconto
    3 - Em até 2x no cartão: preço normal
    4 - 3x ou mais no cartão: 20% de juros
''')

pag = int(input('Digite uma opção: '))

if pag > 4 or pag < 1:
    print('\33[31mOpção inválida!')
else:
    if pag == 1:
        precofinal = preco * 0.9
    elif pag == 2:
        precofinal = preco * 0.95
    elif pag == 3:
        precofinal = preco
    else:
        precofinal = preco * 1.2

    print(f'O valor a ser pago é: R$ {precofinal:.2f}')