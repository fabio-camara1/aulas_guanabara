preço = float(input("qual o preço do produto:"))
desconto = preço - (preço * 0.05)
print("com 5% de desconto o valor fica em R${:.2f}".format(desconto))