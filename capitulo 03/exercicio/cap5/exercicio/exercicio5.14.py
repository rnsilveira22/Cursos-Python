'''
Escreva um programa que leia número inteiros do teclado. O programa
deve ler os números digitados, assim como a soma e a média aritmetrica.
'''

soma, qtNum =0,0


while True:
    num = int(input("Digite número inteiros: "))
    if num == 0:
        break

    soma = soma + num
    qtNum = qtNum+ 1
    media = (soma/qtNum)

print('-- FINAL --\n'
      f'Qt de número digitados: {qtNum}\n'
      f'Soma dos número: {soma}\n'
      f'Média dos número: {media}')