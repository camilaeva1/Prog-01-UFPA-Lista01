#Lista de Exercícios 01  - Questão 13
#Comando: Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
altura = float(input("Insira a sua altura em metros: "))
gen = (input("Insira o seu gênero (F/M): "))
if gen == "F":
  peso = ((62.1*altura) - 44.7)
else:
  peso = ((72.7*altura) - 58)
print("O seu peso ideal é {:.3f} kg.".format(peso))