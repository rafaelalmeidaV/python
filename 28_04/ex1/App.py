from Aluno import *

nome = input("Nome: ")
ra = int(input("RA: "))
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

aluno1 = Aluno(nome, ra, nota1, nota2)

aluno1.calcular_media()

aluno1.descri()