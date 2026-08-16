m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{} m equivalem a: \n{:.2f} km \n{:.2f} hm \n{:.2f} dam \n{:.2f} dm \n{:.2f} cm \n{:.2f} mm'.format(m, km, hm, dam, dm, cm, mm))
