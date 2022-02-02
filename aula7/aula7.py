"""
while em python - aula 7
utilizado para realizar ações enquanto uma condição for verdadeira.

"""
# loop infinito

"""while True:   # nesse modo o loop nunca irá para de rodar.
    nome = input('Digite seu nome: ')
    print(f'Seu nome é: {nome}')"""

"""x = 0  # variável para contar o loop
while x < 10:
    if x == 4:
        x = x + 1
        continue
    print(x)
    x = x + 1
print('Acabou!!!')"""

# Fazendo uma calculadora.

while True:
    nun_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador ou [s] para sair: ')
    if operador == 's':
        break
    if not nun_1.isnumeric() or not num_2.isnumeric():
        print('Digite um número válido, por favor.')
        continue

    nun_1 = int(nun_1)
    num_2 = int(num_2)

    if operador == '+':
        print(nun_1 + num_2)
    elif operador == '-':
        print(nun_1 - num_2)
    elif operador == '/':
        print(nun_1 / num_2)
    elif operador == '*':
        print(nun_1 * num_2)
    else:
        print('Operador inválido')
