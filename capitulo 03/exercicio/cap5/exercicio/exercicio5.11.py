'''
Escreva um programa que pergunte o depósito inicial e taxa de juros de uma poupança
Exiba os valores mês a mês para os 24 primeiros meses
Escreva o total ganho com juros no período.
'''

deposito = float(input("Digite o valo do depósito inicial: R$"))
taxa = float (input("Digite a taxa de juros"))
saldo = deposito
mes = 1
saldo = deposito
while mes<=24:
    saldo = saldo + (saldo * (taxa/100))
    print('Saldo do mes %d é R$%5.2f' %(mes,saldo))
    mes +=1

print('Ganho total com juros foi de R$%5.2f' %(saldo - deposito))
