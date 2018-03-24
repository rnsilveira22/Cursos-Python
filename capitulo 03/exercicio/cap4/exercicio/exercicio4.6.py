"""
Escreva um programa que pergunte a distancia que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$0,50
por km para viagens de até 200km, e R$0.45 para viagens mais longas
"""

distancia = float(input('Digite distancia percorrida'))
if distancia <= 200:
    passagem = 0.50*distancia
else:
    passagem = 0.45*distancia
print('Preço da passagem: R$%7.2f' %passagem)
