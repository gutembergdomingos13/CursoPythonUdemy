"""
Manipulando strings - aula 6
* Strings indices
* Fatiamento de Strings [inicio:fim:passo]
* Funções built-in len, abs type, print, etc...
Essas funções podem ser usadas diretamente em casa tipo.

"""


# positivo     [012345678]
teste_string = 'Gutemberg'
# negativo    -[987654321]

# querendo chamar partes da string seguimos exemplo abaixo.

print(teste_string[1:5])
print(teste_string[-5:-1])
print(teste_string[-9:-4])

nova_string = teste_string[0::2]
print(nova_string)
# para sabermos o tamanho da string podemos usar função 'len'

print(len(teste_string))