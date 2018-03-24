"""
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para viagem.
"""

distancia = float(input("Digite a distância em KM: "))
mediaVelocidade = int(input("Digite qual a velocidade média em Km/h: "))

tempo = distancia/mediaVelocidade

print("Tempo médio da viagem será de: %3.1f horas" %(tempo))

