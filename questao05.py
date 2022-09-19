"""5. Faça um programa Python que receba o preço de custo de um produto e mostre o valor de venda.
Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário."""

valorCusto = float(input("Digite o valor de custo: "))

porcentagem = float(input("Digite a porcentagem de acrescimeto no valor: "))

valorFinal = valorCusto+(valorCusto*porcentagem)/100

print("O valor final do produto é de {:.2f}R$.".format(valorFinal))