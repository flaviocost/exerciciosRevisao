# 8 - Faça um código que receba 4 números e reaalize a soma entre eles e a média entre eles. e mostre o resultado!

soma = 0
for x in range(4):
    num = int(input('informe um valor: '))
    soma = soma + num
    media = soma / 2
print(media)