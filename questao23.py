"""23. Faça um Programa Python para um caixa eletrônico. O programa deverá perguntar ao
usuário a valor do saque e depois informar quantas notas de cada valor serão
fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

valorSaque = float(input("Digite o valor do saque: "))

if 10 <= valorSaque <= 600:

    notas_100 = int(valorSaque // 100)
    valorSaque -= (notas_100 * 100)

    notas_50 = int(valorSaque // 50)
    valorSaque -= (notas_50 * 50)

    notas_10 = int(valorSaque // 10)
    valorSaque -= (notas_10 * 10)

    notas_5 = int(valorSaque // 5)
    valorSaque -= (notas_5 * 5)

    notas_1 = int(valorSaque // 1)
    valorSaque -= (notas_1 * 1)

    print(f"{notas_100} notas de R$100, {notas_50} notas de 50R$, {notas_10} notas de R$10, {notas_5} "
          f"notas de R$5 e {notas_1} notas de R$1.")

else:
    print("Valor abaixo ou acima do limite")
