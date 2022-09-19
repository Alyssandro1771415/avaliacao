"""28. Escreva um programa em Python para ler a capacidade de um elevador (em toneladas)
e o peso total das pessoas em seu interior (em quilogramas). Informar se o elevador
está liberado para subir ou se excedeu a carga máxima."""

capacidade = float(input("Capacidade em Ton: "))
pesoPassageiros = float(input("Peso total dos passageiros: "))

if pesoPassageiros <= capacidade:
    print("Elevador liberado.")
else:
    print("Peso acima do permitido!")