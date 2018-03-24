'''
Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
Pergunte também o valor mensal que será pago.
Imprima o número de meses para que dívida seja paga, o total pago e o total de juros pago.
'''

divida = float(input("Qual o valor da dívida: R$"))
taxa = float(input("Qual a taxa de juros: "))
pagamento = float (input("Qual o valor da mensalidade: R$"))
mes = 1

if(divida *(taxa/100)) > pagamento:
    print('Erro, valor invalido')
else:
    saldo = divida
    juro_pago = 0
    while saldo > pagamento:
        juros = saldo *taxa/100
        saldo = saldo + juros - pagamento
        jurosPago = jurosPago + juros
        print('Saldo da dívida no mês %d é de R$%6.2f. '%(mes,saldo))
        mes = mes + 1
    print('Para pagar a dívida de R$%6.2f, a %.f de juros' %(divida,taxa))
    print('São necessários %d meses, pagando um total de '
          'R$6.2f de juros' %(mes-1, jurosPago))
    print('Saldo residual de R$%6.2f a pagar' %(saldo))