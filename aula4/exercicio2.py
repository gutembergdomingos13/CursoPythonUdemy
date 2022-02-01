"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. EX.:
Bom Dia 0-11, Boa Tarde 12- 17 e Boa Noite 18-23.
"""

hora = input('Digite a hora atual: ')

if hora.isdigit():
    hora = int(hora)
    if hora <= 11:
        print('Bom Dia.')
    elif hora <= 17:
        print('Boa Tarde.')
    elif hora <= 23:
        print('Boa Noite.')
    else:
        print('Hora inválida, por favor digitar horário válido.')
else:
    print('Hora inválida, por favor digitar horário válido.')