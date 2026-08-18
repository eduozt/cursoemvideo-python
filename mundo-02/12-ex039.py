from datetime import date

nasc = int(input('Digite o ano do seu nascimento: '))
anoalistamento = nasc + 18
anoatual = date.today().year

dif = anoatual - anoalistamento

if dif == 0:
    print('Você deve se alistar esse ano!')
elif dif < 0:
    print(f'Você deve se alistar daqui a {abs(dif)} anos.')
else:
    print(f'Seu alistamento foi há {dif} anos.')