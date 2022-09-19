"""21. Faça um Programa Python que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um
triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro; Triângulo Equilátero: três lados iguais; Triângulo isósceles: quaisquer dois
lados iguais; Triângulo Escaleno: três lados diferentes; """

ladoA = float(input("Lado A:"))
ladoB = float(input("Lado B:"))
ladoC = float(input("Lado C:"))

if ladoA+ladoB > ladoC and ladoA+ladoC > ladoB and ladoB+ladoC > ladoA:
    if ladoA == ladoB and ladoA == ladoC:
        print("Triângulo equilátero.")
    elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("Os valores não implicam num triângulo.")