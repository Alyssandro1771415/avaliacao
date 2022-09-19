"""16. Faça um Programa Python que leia três números e mostre o maior deles."""

valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite um valor: "))
valor3 = float(input("Digite um valor: "))

maiorValor = valor1

if valor2 > maiorValor:
    maiorValor = valor2
if valor3 > maiorValor:
    maiorValor = valor3

print(f"O maior valor é {maiorValor}.")