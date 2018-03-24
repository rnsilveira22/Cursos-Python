'''
Escreva um programa e digite todas as resposta corretas, depois tente com resposta diferentes.
Veja que estamos .....
'''

pontos = 0
questao = 1

while questao<=3:
    resposta = input("Resposta da questão %d:" %questao)
    if questao == 1 and (resposta == 'B' or resposta == 'b'):
        pontos = pontos + 1
    if questao == 2 and (resposta == 'A' or resposta == 'a'):
        pontos = pontos + 1
    if questao == 3 and (resposta == 'D' or resposta == 'd') :
        pontos = pontos + 1
    questao +=1
print("O aluno fez %d ponto(s)" %pontos)