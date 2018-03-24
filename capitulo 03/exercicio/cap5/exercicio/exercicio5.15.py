'''
Escreva um programa para controlar um pequena máquina resgistradora.
Você deve solcitar ao usuario que digite o codigo do produto e a quantidade
comprada. Utilize a tabela a baixo de codigos para obetr o preço de cada produto;

'''

valorPagar = 0
while True:
    codigo = int(input("Digite código da mercadoria: "))
    preço = 0.0
    if codigo == 0:
        break
    elif codigo ==1:
        preço = 0.50
    elif codigo ==2:
        preço = 1.00
    elif codigo ==3:
        preço = 4.00
    elif codigo ==5:
        preço = 7.00
    elif codigo ==9:
        preço = 8.00
    else:
        print('Código Invalido!')

    if preço != 0:
        quantidade = int(input("Quantidade: "))
        valorPagar = valorPagar + (preço*quantidade)

print('+'*30)
print(f'Total a pagar: R${valorPagar:.2f}')