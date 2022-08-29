#Lista de Exercícios 01  - Questão 12
#Comando: Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Insira a sua altura em metros: "))
peso = ((72.7 * altura) - 58)
print("O seu peso ideal é {:.3f} kg.".format(peso))