"""Escreva um programa para aprovar o emprestimo bancario para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar
O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação
como sendo o valor da casa a comprar dividido pelo número de meses a pagar."""

salario = float(input('Digite seu salário : R$'))
valorImovel = float(input('Digite o valor do imóvel: R$'))
tempoPagar = int(input('Digite em quantos anos vocês pagar: '))

valorParcela = valorImovel/(tempoPagar*12)

if valorParcela> (salario*0.3):
    print('Valor das parcelas ultrapassa 30% do seu salário')
else:
    print('Você ira pagar %d vezes de R$%6.2f.'%((tempoPagar*12), valorParcela))


