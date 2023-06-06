numero = int(input("digite aqui um numero: ")) # jeito matematico de resolver
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"milhar:{m}\ncentena:{c}\ndezena:{d}\nunidade:{u}")

