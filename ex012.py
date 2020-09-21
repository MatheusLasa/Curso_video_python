n1 = float(input("Qual é o preço do produto? R$"))
d = n1 - (n1*5/100)
print("O produto que custava R${}, agora na promoção com 5% de desconto vai custar R${:.2f}".format(n1,d))
