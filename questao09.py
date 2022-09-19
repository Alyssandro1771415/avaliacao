"""9. Faça um Programa Python que peça 2 números inteiros e um número real. Calcule e
mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo."""

inteiro_1 = int(input("Digite um número inteiro: "))
inteiro_2 = int(input("Digite um número inteiro: "))
real = float(input("Digite um número real: "))

valorA = inteiro_1*2 + inteiro_2/2
valorB = inteiro_1*3 + real
valorC = real**3

print("O produto do dobro do primeiro com metade do segundo: {:.2f}".format(valorA))
print("A soma do triplo do primeiro com o terceiro: {:.2f}".format(valorB))
print(" terceiro elevado ao cubo: {:.2f}".format(valorC))