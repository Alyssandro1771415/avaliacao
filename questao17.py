"""17. Faça um programa Python que pergunte o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. """

produto1 = float(input("Digite o valor do 1° produto:"))
produto2 = float(input("Digite o valor do 2° produto:"))
produto3 = float(input("Digite o valor do 3° produto:"))

maisBarato = produto1

if produto2 < maisBarato:
    maisBarato = produto2
if produto3 < maisBarato:
    maisBarato = produto3

print(f"O produto mais barato custa R${maisBarato}")