nome = input("digite o seu nome completo: ").strip()
print(f"seu nome em maiusculo é {nome.upper()}")
print(f"seu nome em nimnusculo é {nome.lower()}")
print("seu nome tem ao todo {} letras".format(len(nome)-nome.count(" ")))  # usar o cout - " " faz ele retirar vazios
print(f"seu primeiro nome tem {nome.find(' ')}")
separa = nome.split()
print(f"seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras")
