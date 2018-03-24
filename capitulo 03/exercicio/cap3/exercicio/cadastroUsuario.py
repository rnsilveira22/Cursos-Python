'''
Criar um programa cadastroUsuario.py contendo os seguintes dados:
nome, idade, cpf, identidade, nacionaliade, naturalidade, endereço, sexo, time de futebol e profissão.
o mesmo deve ter três saidas, uma pessoa(nome, idade, time de futebol) outra profissional ( nome,
identidade, cpf e profissão) e por ultimo uma completa exibindo todos os dados.
'''

# -*- coding: utf8 -*-

nome = input('Digite seu nome: ')
cpf = int(input('Digite seu CPF: '))
rg = int (input('Digite seu RG: '))
idade = int(input('Digite sua idade: '))
nacionalidade = input('Digite sua naciolidade: ')
naturalidade = input('Digite sua naturalidade: ')
endereco = input('Digite nome da rua: ')
sexo = input('Digite eu sexo: (M = Masculino ou F = Feminino)? ')
time = input('Qual o seu time de futebol? ')
profissao= input('Qual a sua profissão? ')


print('-'*10,'Pessoal','-'*10,'\n'
                              'nome = {}\n'
                              'idade = {}\n'
                              'time de futebol = {}'.format(nome, idade, time))
print('-'*10,'Profissional','-'*10,'\n'
                              'nome = %s\n'
                              'rg = %d\n'
                              'cpf = %d\n'
                              'profissão = %s'%(nome, rg, cpf,profissao))
print('-'*10,'Cadastro Completo','-'*10,'\n'
                                        'Nome: %s - CPF: %d - RG: %d\n'
                                        'Idade: %d - Sexo: %s\n'
                                        'Mora na rua: %s\n'
                                        'Nacionalidade: %s - Naturaliade: %s\n'
                                        'Torce para o time: %s\n'
                                        'Profissição: %s'% (nome, cpf, rg,
                                                            idade, sexo,
                                                            endereco,
                                                            nacionalidade, naturalidade,
                                                            time,
                                                            profissao))