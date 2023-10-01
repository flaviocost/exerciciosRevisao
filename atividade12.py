# Escreva um algoritmo para ler o
# número total de eleitores de um
# município, o número de votos brancos,
# nulos e válidos. Calcular e escrever o
# percentual que cada um representa em
# relação ao total de eleitores.

totalEleitores = int(input('Informe o total de eleitores do município: '))
votoBrancos = int(input('Informe os votos em branco: '))
votoNulos = int(input('Informe os vatos nulos: '))
votosValidos = int(input('Informe os votos válidos: '))

porcentagemBrancos = (votoBrancos / totalEleitores) * 100
porcentagemNulos = (votoNulos / totalEleitores) * 100
porcentagemValidos = (votosValidos / totalEleitores) * 100


print(f'O percentual de votos em brancos foi {porcentagemBrancos:.1f}%')
print(f'O percentual de votos nulos foi {porcentagemNulos:.1f}%')
print(f'O percentual de votos em válidos foi {porcentagemValidos:.1f}%')

