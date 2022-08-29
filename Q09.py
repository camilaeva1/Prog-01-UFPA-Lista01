#Lista de Exercícios 01  - Questão 09
#Comando: Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
f = (float(input("Insira a temperatura em Fahrenheit:  ")))
c = 5 * ((f-32) / 9)
print("A temperatura inserida corresponde a {:.3f} celsius.".format(c))