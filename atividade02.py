# 2 - Crie um código que leia um número diferente de zero(0) e diga se este número é positivo ou negativo!

num1 = int(input('Informe um valor: '))

if num1 != 0:
    if num1 < 0:
        print(f'{num1} é negativo!')
    else:
        print(f'{num1} é positivo!')
else:
    print('Valor inválido!')