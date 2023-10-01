# 6 - Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10 caso contrário escrever NÃO É MAIOR QUE 10!

num = int(input('Informe um valor: '))

if num != 10:
    if num > 10:
        print('É maior que 10!')
    else:
        print('É menor que 10!')
else:
    print(f'Oshe boy, {num} é igual a 10!')