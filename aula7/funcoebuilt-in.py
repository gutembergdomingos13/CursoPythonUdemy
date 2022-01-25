
# Sempre consultar a documentação do python

num1 = input('Digite um número: ')
num2 = input('Digite mais um número: ')

#num1 = int(num1)
#num2 = int(num2)

# para saber se num1 ou num2 pode ser convertido para int usamos as funções: isdigit, isnumeric ou isdecimal
# Nesse caso usando essas três funções não pode ser número float nem número negativo.

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Valores inválidos, não pude converter os números.')

