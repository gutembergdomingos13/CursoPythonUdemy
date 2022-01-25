

num1 = input('Digite um número: ')
num2 = input('Digite mais um número: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('Valores inválido, não pude converter os números.')
