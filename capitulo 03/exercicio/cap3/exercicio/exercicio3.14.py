"""
Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.
"""
diaria = int(input("Quantas diarias foram utilizadas? "))
kmUsada = float(input('Qual a distancia percorrida? '))

valorPagar = (diaria*60)+(kmUsada*0.15)

print('++++Fatura do aluguel+++++++\n'
      'qtde de diarias = %d dia(s)\n'
      'km utilizados = %4.2f km(s)\n'
      'Total a pagar R$%4.2f'%(diaria,kmUsada,valorPagar))