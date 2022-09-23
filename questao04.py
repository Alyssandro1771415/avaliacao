"""4. Uma loja está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um programa
Python que receba um valor de uma compra e mostre o valor das prestações."""
try:
    valor = float(input("Digite o valor total da compra: "))
    if valor < 0:
        exit()
    prestacao = valor/5

    print("O valor de cada uma das cinco prestações será de {:.2f}R$".format(prestacao))
except:
    print("Digite um valor numérico e positivo!")
