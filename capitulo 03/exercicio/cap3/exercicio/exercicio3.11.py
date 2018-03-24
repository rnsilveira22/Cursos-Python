"""
Faça um programa que solicite o preço de uma mercadoria e o percentual
de desconto. Exiba o valor do desconto e o preço  a pagar.
"""

preco = float(input("Valor do produto: "))
desconto = int(input("Valor do desconto: "))

novoPreco = preco - (preco*(desconto/100))

print("+"*30+"\n"
             "Desconto = {}%\n"
             "Total a pagar = {}".format(desconto, novoPreco))