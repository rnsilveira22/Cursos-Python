'''
Modifique o programa anterior de forma que o usúario também digite o inicio e o fim da tabuada, em vez
de comerçar em 1 e 10.
'''

n = int(input("Tabuada de: "))
inicio = int(input('Digite inicio: '))
fim = int(input('Digite fim: '))
x = inicio
while  x<=fim:
    print ('{} X {} = {}'.format(n , x ,(n*x)))
    x = x+1