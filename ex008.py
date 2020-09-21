n1 = float(input('Dígite uma distância em metros: '))
print('A medida corresponde a {} metros'.format(n1))
km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000
print('km = {}\nhm = {}\ndam = {}\ndm = {}\ncm = {}\nmm = {}'.format(km, hm, dam, dm, cm, mm))
