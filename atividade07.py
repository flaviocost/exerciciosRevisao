# 7 - Faça um código que receba o valor da base e da altura de um triângulo e calcule sua área. usando a fórmula A = (BASE X ALTURA) /2
loop = 's'
while loop == 's' or loop == 'S':

    base = int(input('Informe o valor da Base do triângulo: '))
    while base == 0:
        base = int(input('Putz, valor inválido, informe outro valor: '))
    altura = int(input('Informe o valor da Altura do triângulo: '))
    while altura == 0:
        altura = int(input('De novo?! Informe outro valor:  '))

    area = (base + altura)/2
    print(f'Sua área é {area}')
    loop = input('Deseja encerrar o programa, s/n:')
print('Programa finalizado!')

