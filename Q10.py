#Lista de Exercícios 01  - Questão 10
#Comando: Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
c = (float(input("Insira a temperatura em Celsius:  ")))
f =  (c * 1.8) + 32
print("A temperatura inserida corresponde a {:.3f} Fahrenheit.".format(f))