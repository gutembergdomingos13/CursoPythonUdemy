"""
Formatando valores com modificadores
:s - Textos (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(Número)f - quantidade de casas decimais (float) ex.: (:.2f)
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - posicionado a esquerda
< - posicionado a direita
^ - posicionado no centro
"""

nome = 'gutemberg domingos'
sobrenome = 'domingos'.capitalize()
caracteres = 50

print(f'{sobrenome:@^{caracteres}}')
print(f'{nome:#^50}')