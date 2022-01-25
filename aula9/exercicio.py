
"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    numeroResults = numero % 2
    if numeroResults == 0:
        print('O número digitado é PAR. ')
    else:
        print('O número digitado é ÍMPAR')

else:
    print('O número digitado não é um número inteiro.')
