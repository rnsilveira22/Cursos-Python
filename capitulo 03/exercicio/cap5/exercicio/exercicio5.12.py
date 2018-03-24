'''
Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no inicio de cada mês,
e você deve considera-lo para calculo de juros do mês seguinte.
'''

deposito = float(input("Digite o valo do depósito inicial: R$"))
taxa = float (input("Digite a taxa de juros"))
saldo = deposito
mes = 1
saldo = deposito
novoDeposito = 0
while mes<=24:
    saldo = saldo + (saldo * (taxa/100))
    print('Saldo do mes %d é R$%5.2f .' %(mes,saldo))
    mes +=1
    novoDeposito = float(input('Qual valor você depositar?'))
    saldo = saldo+novoDeposito
print('Ganho total com juros foi de R$%5.2f' %(saldo - deposito))
