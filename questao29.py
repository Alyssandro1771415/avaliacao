"""29. Desenvolver um programa em Python para calcular a conta de água para a
CAGEPA. O custo da água varia dependendo se o consumidor é residencial,
comercial ou industrial. A regra para calcular a conta é:
– Residencial: R$50,00 de taxa mais R$0,05 por m³ gastos; – Comercial: R$500,00 para os primeiros 80 m³ gastos mais R$0,25 por m³
gastos acima dos 80 m³; – Industrial: R$800,00 para os primeiros 100 m³ gastos mais R$0,04 por m³
gastos acima dos 100 m³;
O programa deverá ler o número da conta do cliente, consumo de água por
metros cúbicos e o tipo de consumidor (residencial, comercial e industrial).
Como resultado, imprima o número da conta do cliente e o valor real a ser pago
pelo mesmo"""

numeroConta = int(input("Número da conta: "))
consumo = float(input("Consumo em m³: "))
tipoConsumidor = int(input("Digite o número correspondente tipo correspondente:\n"
                           "1 - residencial\n"
                           "2 - comercial\n"
                           "3 - industrial\n"))
valorPagar = 0

if tipoConsumidor == 1:
    valorPagar = 50 + 0.05 * consumo

elif tipoConsumidor == 2:
    if consumo < 80:
        valorPagar = 500
    else:
        valorPagar = 500 + (0.25*(consumo-80))

elif tipoConsumidor == 3:
    if consumo <= 100:
        valorPagar = 800
    else:
        valorPagar = 800 + (0.04*(consumo-100))

else:
    print("Tipo inválido, tente novamente.")
    exit()

print(f"O cliente {numeroConta} pagará R${valorPagar}.")
