# -*- coding:utf8 -*-

dia = int(input('Digite quantidade de dias: '))
hora = int(input('Digite a quantidade de horas: '))
minuto = int(input('Digite a quantidade de minutos: '))
segundo = int(input('Digite a quantidade de segundos: '))

qtSegundo = ((((((dia*24)+hora)*60)+minuto)*60)+segundo)

print('Resultado\n'
      '{} dias,'
      '{} horas,'
      '{} minutos,'
      '{} segundos'
      ' é igual a {} segundos'.format(dia,hora,minuto,segundo,qtSegundo))