# 1. Faça um Programa Python que converta metros para centímetros.

try:
    metros = float(input("Digite um valor em metros: "))

    if metros > 0:
        centimetros = metros*100
        print("A conversão de {}m para centimetros é {:.2f}cm.".format(metros, centimetros))
    else:
        print("Valor inválido, reinicie o programa e digite um número válido.")
        exit()
except:
    print("reinicie o programa e digite um valor numérico!")