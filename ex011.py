n1 = float(input('Largura da parede:'))
n2 = float(input('Altura da parede:'))
a = n1 * n2
print('Sua parede tem a dimensão {}x{} e sua área é de {}m²'.format(n1, n2, a))
t = a / 2
print('Você vai precisar de {}l de tinta'.format(t))
