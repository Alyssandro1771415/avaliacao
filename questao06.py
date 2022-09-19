"""6. Escrever um programa Python para determinar o consumo médio de um automóvel
sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto."""

Km = float(input("Digite a distância em KM: "))

combustivel = float(input("Digite quanto de combustível foi consumido em litros: "))

consumoMedio = combustivel/Km

print("O consumo médio de seu altomóvel é de {:.2f}L/Km".format(consumoMedio))