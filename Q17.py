import math
#Lista de Exercícios 01  - Questão 17
#Comando: Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
mq1 = float(input("Insira o tamanho (m²) da área a ser pintada: "))
galoes = (mq1/21.6)
latas = (mq1/108)
if mq1 <= 21.6:
  print("Você precisará de 1 galão de tinta, e pagará R$ 25.")
if (mq1 > 21.6) and (mq1 <= 64.8):
  galoes = round(galoes+0.5)
  pagar = galoes * 25
  print("Você precisará de {} galões de tinta e pagará R$ {}.".format(galoes, pagar))
elif mq1 > 64.8:
  mq2 = mq1 * 1.1
  l = mq2/6
  latas1 = l/18
  latas2 = round(latas1, 0)
  precolata2 = latas2 * 80
  faltatinta = latas1 - latas2
  litro = round(faltatinta, 3) * 18
  galoes1 = litro/3.6
  galoes2 = math.ceil(galoes1)
  precogaloes2 = galoes2 *25
  print("Você precisará de {} lata(s) e {} galão (ões).".format(latas2, galoes2))
  print("Total a pagar = R${}".format(precolata2 + precogaloes2))