casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual a sua renda mensal? '))
anos = int(input('Em quantos anos deseja pagar? '))

qtdeparcelas = anos * 12
parcelamaxima = salario * 0.3
valorparcela = casa / qtdeparcelas

if valorparcela > parcelamaxima:
    print(f'Empréstimo negado! O valor da parcela ficaria {valorparcela:.2f} e a parcela máxima que você poderia pagar é {parcelamaxima:.2f}')
else:
    print(f'Você pagará {qtdeparcelas} parcelas de R$ {valorparcela:.2f}.')
