import random
aluno1 = input("digite o nome do primeiro aluno:")
aluno2 = input("digite o nome do segundo aluno:")
aluno3 = input("digite o nome do terceiro aluno:")
aluno4 = input("digite o nome do quarto aluno:")
classe = [aluno1, aluno2, aluno3, aluno4]
apagar_o_quadro = random.choice(classe)
print(f"quem ira apagar o quadro é:{apagar_o_quadro}")

meus_alunos = ["fabio", "leo", "paulo", "luiz"]
import random
meus_alunos = input("digite aqui o nome dos seus alunos:")
meus_alunos2 = meus_alunos.split()
meus_alunos3 = set(meus_alunos2)
print(random.choice(meus_alunos3))