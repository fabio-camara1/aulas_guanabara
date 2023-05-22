import math
cateto_oposto = float(input("qual o comprimentodo do cateto oposto? "))
cateto_adjacente = float(input("qual o comprimento do cateto adjacente? "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"a hipotenusa do seu triangulo retangulo é {hipotenusa:.2f}")
