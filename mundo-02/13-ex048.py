s = 0
cont = 0
for c in range(0,500,3):
    if c % 2 == 1:
        s = s + c
        cont = cont + 1
    #print(c)
print(f'Entre 1 e 500 existem {cont} números ímpares divisíveis por 3 e a soma dele é {s}.')