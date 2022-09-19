"""14. Na fazenda de João são criadas aves. Para alimentá-las ele compra sacas de ração cujo
peso é fornecido em quilos. No total ele tem dois grupos de aves, para os quais
fornece a quantidade de ração em gramas. A quantidade diária de ração fornecida
para cada grupo de aves é sempre a mesma. Faça um programa em Python que receba
o peso do saco de ração e a quantidade de ração fornecida para cada grupo de aves,
calcule e mostre quanto restará de ração após uma semana"""

pesoRacao = float(input("Peso em Kg do saco de ração: "))
quantidadeRacao = float(input("Quantidade de ração para as aves em gramas: "))

restaRacao = pesoRacao*1000 - (quantidadeRacao*2*7) #Dois grupos de aves, 7 dias da semana.

if restaRacao > 0:
    print("Quantidade de ração restante: {:.2f}gramas.".format(restaRacao))
elif restaRacao == 0:
    print("A quantidade de ração foi exata à demanda.")
else:
    restaRacao*=-1 #Convertendo para positivo para mostrar o valor que resta sem o símbolo de menos.
    print("A quantidade de ração foi insuficiente, faltaram {:.2f}gramas de ração.".format(restaRacao))
