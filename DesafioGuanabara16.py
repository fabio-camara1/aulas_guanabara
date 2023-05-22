import math
angulo = float(input("digite aqui o angulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"o angulo de {angulo :.2f} tem o:\nseno{seno :.2f}\ncosseno{cosseno :.2f}\ntangente{tangente :.2f}")
