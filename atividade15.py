# Escreva um algoritmo para ler dois valores (considere que não serão lidos e escrevê-los em ordem
# crescente

num1 = int(input('Informe um valor: '))
num2 = int(input('Informe outro valor: '))
while num1 == num2:
    print('Os valores não podem ser iguais!')
    num1 = int(input('Informe o primeiro valor novamente: '))
    num2 = int(input('Informe o segundo valor novamente: '))
else:
    if num1 > num2:
        print(f'Em ordem crescente {num1}, {num2}')
    else:
        print(f'Em ordem crescente {num2}, {num1}')