"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva
"Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
e se for maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu primeiro nome: ').strip()
letrasNome = len(nome)

if letrasNome <= 4:
    print('Seu nome é muito curto.')
elif letrasNome <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
