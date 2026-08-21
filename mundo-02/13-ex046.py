from time import sleep

for c in range (10, 0, -1):
    print(f'{c}...')
    sleep(1)
print('\33[31mFogos estourando!!!!!!')