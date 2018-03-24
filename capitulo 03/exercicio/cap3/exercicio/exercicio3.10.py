"""
Faça um programa que calcule o aumento de salário. Ele deve solicitar
o valor do salário e a porcetagem do aumento. Exiba o valor do aumento e o novo salário.
"""

salario = float(input('Qual o valor do salário? '))
aumento = int(input("Qual a porcetagem de aumento? "))

novoSalario = salario +(salario*(aumento/100))

print("-"*30+"\n"
      "O aumento foi de %d %% \n"
      "Novo salário é: R$ %7.2f" %(aumento, novoSalario))

