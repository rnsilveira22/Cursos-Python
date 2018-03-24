"""
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade
de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10
minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

qtCigarros = float(input('Digite a quantidade de cigarros fumados por dia: '))
qtAnos = float(input('Digite a quantidade de anos fumando: '))

reducaoMinutos = ((qtAnos*365)*qtCigarros)*10

reducaoEmDias = reducaoMinutos / (24*60)


print('Você já perdeu %d dias da sua vida' %reducaoEmDias)

