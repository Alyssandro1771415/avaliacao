"""2. Faça um Programa Python que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

valorHora = float(input("Digite o valor que você ganha por hora de trabalho: "))
horas = int(input("Digite quantas horas de trabalho você executa por mês: "))

valorTotal = valorHora*horas

print("O seu salario mensal é de {:.2f}R$.".format(valorTotal))