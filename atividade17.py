# As maçãs custam R$ 1,30 cada se forem
# compradas menos de uma dúzia, e R$ 1,00
# se forem
# compradas pelo menos 12. Escreva um
# programa que leia o número de maçãs
# compradas, calcule e
# escreva o custo total da compra

loop = 's'
print('<MENU DE MAÇAS APPLE PE>\nUnidades de Maças = R$ 1,30\nDúzia de Maças = R$ 1,00')
while loop == 's' or loop == 'S':
    macas = int(input('Informe quantas maças deseja comprar: '))
    macasMeiaduzia = 1.30
    macasDuzia = 1
    if macas < 12:
        print(f'O valor total a pagar é {macasMeiaduzia * macas:.2f}')
    else:
        print(f'O valor total a pagar é {macasDuzia * macas}')
    loop = input('Deseja realizar uma nova compra, s/n: ')
print('Apple PE, agradece pelas compras, volte sempre!')