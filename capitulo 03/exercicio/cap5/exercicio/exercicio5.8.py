'''
Escreva um programa que leia dois número, Imprima o resultado da
multiplicação do primeiro pelo segundo, Utilize apenas os operadores de soma e subtração
para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números
como a soma sucessiva de um deles. Assim, 4X5 = 5+5+5+5 = 4+4+4+4+4.
'''


num1 = int(input('Digite 1º numero: '))
num2 = int(input('Digite 2º numero: '))

x = 1
while x<=num1:
    print (num2,end="+")
    x +=1
