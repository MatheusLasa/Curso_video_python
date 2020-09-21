salar = float(input('Qual é o salário do funcionário? R$ '))
aumen = salar + (salar*15/100)
print('O salário do funcionário é de R${}, e com 15% de aumento, passa a receber R${:.2f}'.format(salar, aumen))