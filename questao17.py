"""17. Faça um programa Python que pergunte o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. """

produto1 = float(input("Digite o valor do 1° produto:"))
if produto1 > 0:
    produto2 = float(input("Digite o valor do 2° produto:"))
    if produto2 > 0:
        produto3 = float(input("Digite o valor do 3° produto:"))
        if produto3 > 0:
            maisBarato = produto1
            if produto2 < maisBarato:
                maisBarato = produto2
            if produto3 < maisBarato:
                maisBarato = produto3

            print(f"O produto mais barato custa R${maisBarato}")
        else:
            print("Valor inválido, informe um positivo!")
            exit()
    else:
        print("Valor inválido, informe um positivo!")
        exit()
else:
    print("Valor negativo, informe um valor válido!")
    exit()
