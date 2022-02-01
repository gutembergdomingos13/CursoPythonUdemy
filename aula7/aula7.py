"""
while em python - aula 7
utilizado para realizar ações enquanto uma condição for verdadeira.

"""
# loop infinito

"""while True:   # nesse modo o loop nunca irá para de rodar.
    nome = input('Digite seu nome: ')
    print(f'Seu nome é: {nome}')"""

x = 0  # variável para contar o loop
while x < 10:
    if x == 4:
        x = x + 1
        continue
    print(x)
    x = x + 1
print('Acabou!!!')