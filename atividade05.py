# 5 - Crie um algoritmo que leia um número e diga se ele é par ou impar
loop = 's'
while loop == 's' or loop == 'S':
    num = int(input('Informe um valor: '))
    if num % 2 == 0:
        print(f'{num} é par!')
    else:
        print(f'{num} é impar!')
    loop = input('Deseja tentar novamente com outro valor s/n: ')
print('Programa finalizado!')