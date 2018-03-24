"""
Escreva um programa que pergunte o salario do funcionario e calcule
o valor do aumento. Para salario superiores a R$1250,00, calcule um aumento de 10%. Para inferiores
ou iguais, de 15%.
"""

salario = float(input('Digite salario'))
novoSalario = 0

if salario<=1250:
    novoSalario = salario+(salario*0.15)
    print ("Salario Antigo era de R$%7.2f\n"
           "Seu aumento será de 15%%\n"
           "Seu novo salario será de R$%7.2f" %(salario,novoSalario))
else:
    novoSalario = salario+(salario*0.10)
    print("Salario Antigo era de R$%7.2f\n"
          "Seu aumento será de 10%%\n"
          "Seu novo salario será de R$%7.2f" % (salario, novoSalario))