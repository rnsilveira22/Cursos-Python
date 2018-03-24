"""Escreva um programa que calcule o preço a pgar pelo fornecimento de energia elétrica.
Pregunte a quantidade kWh consumida e o tipo de instalação: R para residencia, I para indútria,
e C para comécios. Calcule o preço a pagar de acordo com a tabela a seguir.
resid = cons.<=500 kWh - 0.40$
resid = cons.>500 kWh  = 0.65$
comerc = cons.<=1000 kWh - 0.55$
comerc = cons.>1000 kWh  = 0.60$
indus = cons.<=5000 kWh - 0.55$
indus = cons.>5000 kWh  = 0.60$"""


qtdConsumo = int(input("Digite o quantidade de consumo em kWh: "))
tipoUnidade = input("Digite o tipo da unidade consumidora:\n"
                    "R = Residência\n"
                    "C = Comércio\n"
                    "I = Indútria\n")

if tipoUnidade == 'R'or tipoUnidade == 'r':
    print ("----Unidade Consumidora RESIDÊNCIA----")
    if qtdConsumo<500:
        valorPagar = float(qtdConsumo*0.4)
        print('Seu consumo foi : %d kWh \n'
             'Valor a pagar: R$%6.2f' %(qtdConsumo,valorPagar))
    else:
        valorPagar = float(qtdConsumo*0.65)
        print(f'valor a pagar {valorPagar:8.2f}')
if tipoUnidade == 'C'or tipoUnidade == 'c':
    print("----Unidade Consumidora COMÉRCIO----")
    if qtdConsumo<1000:
        valorPagar = float(qtdConsumo*0.55)
        print(f'valor a pagar {valorPagar:8.2f}')
    else:
        valorPagar = float(qtdConsumo*0.60)
        print(f'valor a pagar {valorPagar:8.2f}')

if tipoUnidade == 'I' or tipoUnidade == 'i':
    print("----Unidade Consumidora INDÚSTRIA----")
    if qtdConsumo<5000:
        valorPagar = float(qtdConsumo*0.55)
        print(f'valor a pagar {valorPagar:8.2f}')
    else:
        valorPagar = float(qtdConsumo*0.60)
        print(f'valor a pagar {valorPagar:8.2f}')


else:
    preco = 0
    print('Erro! Tipo de unidade consumidora invalida!')

    
#print('Seu consumo foi : %d kWh \n'
#      'Valor a pagar: R$%6.2f' %(qtdConsumo,valorPagar))

#print(f'valor a pagar {valorPagar:8.2f}')