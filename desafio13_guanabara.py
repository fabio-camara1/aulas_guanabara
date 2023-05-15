km = float(input("quantos km foram percorridos com o carro? "))
dia = int(input("quantos dias o carro passo alugado? "))
pagamento = (km * 0.15) + (dia * 60)
print("o pagamento pelo aluguel do veiculo fica em:R${:.2f}".format(pagamento))
