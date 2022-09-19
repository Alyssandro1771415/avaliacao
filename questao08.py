"""8. Escrever um programa Python que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas
por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas
, informar o seu nome, o salário fixo e salário no final do mês."""

nome = str(input("Nome do vendedor: "))
salarioFixo = float(input("Digite o valor fixo de salário: "))
totalVendas = float(input("Digite o valor total de vendas no mês: "))

porcentagem = 0.15

salarioFinal = salarioFixo+totalVendas*porcentagem

print("O salario finao de {} é {}R$".format(nome, salarioFinal))