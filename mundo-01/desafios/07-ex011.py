l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))

area = l * a
tinta = area / 2

print('Sua parede tem {} metros quadrados e você precisa de {} litros de tinta para pintá-la.'.format(area, tinta))
