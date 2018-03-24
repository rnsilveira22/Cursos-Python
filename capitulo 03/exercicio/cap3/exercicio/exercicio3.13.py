"""
Estreca um programa que converta uma temperatura digitada em
ºC em ºF. A formula para essa conversão é: F = (9 X C)/5 + 32.
"""

celsus = float(input("Digite temperatura em graus celsus: "))

fahrenheit = (9*celsus)/5+32

print("++"*20+'\n ____RESULTADO_____\n{}ºC = {}ºF'.format(celsus,fahrenheit))