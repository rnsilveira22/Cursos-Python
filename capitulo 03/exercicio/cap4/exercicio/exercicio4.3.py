"""
Escreva um programa que leia três números e que imprima o maior e o menor.
"""

a= int(input("Primeiro valor: "))
b= int(input("segundo valor: "))
c= int(input("terceir valor: "))
maior = a
menor = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
if b<a and b<c:
    maior = b
if c<a and c<b:
    maior = c
print('Maior valor= ',maior)
print('Menor valor= ',menor)