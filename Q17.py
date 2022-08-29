#Lista de Exercícios 01  - Questão 17
#Comando: Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
mq = float(input("Insira o tamanho (m²) da área a ser pintada: "))
galoes = (mq/21.6)
latas = (mq/108)
if mq <= 21.6:
  print("Você precisará de 1 galão de tinta, e pagará R$ 25.")
if (mq > 21.6) and (mq <= 64.8):
  galoes = round(galoes+0.5)
  pagar = galoes * 25
  print("Você precisará de {} galões de tinta e pagará R$ {}.".format(galoes, pagar))
if mq > 64.8:
  if latas <= 1: 
    print("Você precisará de 1 lata de tinta, e pagará R$ 80.")
  else:
    latas = round(latas+0.5)
    pagar = latas * 80
    print("Você precisará de {} latas de tinta e pagará R$ {}.".format(latas, pagar))  
   