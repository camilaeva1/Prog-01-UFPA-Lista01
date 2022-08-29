#Lista de Exercícios 01  - Questão 08
#Comando: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
v1 = (float(input("Quanto você ganha por hora?  ")))
hora = (int(input("Quantas  horas ganha trabalha por mês?  ")))
sal = v1 * hora
print("O seu salário no referido més é de R$ {}.".format(sal))