"""27. O IPVA é calculado de acordo com o tipo de veículo, cuja alíquota é definida por cada
Estado sobre o valor venal do carro de acordo com a Tabela Fipe (Fundação Instituto
de Pesquisas Econômicas), variando entre 1% e 4%. Escreva um programa em Python
para calcular o valor do IPVA de um veículo com base nas informações a seguir:"""

print("Digite o número correspondente ao seu tipo de veículo:\n"
      "1 - automóveis\n"
      "2 - Caminhões de carga e furgão\n"
      "3 - Automóveis para transporte público\n"
      "4 - Motocicletas\n"
      "5 - Veículos de locadoras\n"
      "6 - Ônibus, micro-ônibus, caminhão, caminhão trator")

tipoVeiculo = int(input("Tipo: "))
valorVenal = float(input("Valor Venal: "))
IPVA = 0

if tipoVeiculo == 1:
      IPVA = valorVenal * 0.04
elif tipoVeiculo == 2:
      IPVA = valorVenal * 0.03
elif tipoVeiculo == 3:
      IPVA = valorVenal + 0.02
elif tipoVeiculo == 4:
      IPVA = valorVenal * 0.02
elif tipoVeiculo == 5:
      IPVA = valorVenal * 0.01
elif tipoVeiculo == 6:
      IPVA = valorVenal * 0.01

print(f"O valor de seu IPVA é: {IPVA}")