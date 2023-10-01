# 4 - Crie um algoritmo que receba 3 números e informe qual o maior entre eles

num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
num3 = int(input('Informe o terceiro valor: '))

if num1 > num2:
    if num1 > num3:
        print(f'{num1} é maior!')
    else:
        print(f'{num3} é maior')
elif num2 > num3:
    print(f'{num2} é maior!')
else:
    print(f'{num3} é maior!')
