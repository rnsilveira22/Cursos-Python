"""
 Escreva um programa que leia dois numeros e que pergunte qual operação você deseja realizar.
 Você deve poder calcular a soma(+), subtração (-), multiplicação (*) e divisão (/). Exiba
 o resultado da operação solicitada.
"""
a = float(input('primeiro numero'))
b = float(input('segundo numero'))

operacoes = input('Digite a operacoes desejadas(+,-,/,*):')
if operacoes == "+":
    resultado = a + b
elif operacoes == "-":
    resultado = a - b
elif operacoes == "*":
    resultado = a * b
elif operacoes == "/":
    resultado = a / b
else:
    print("Operação invalida")

print("Resultado da operação matematica:", resultado)