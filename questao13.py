"""13. Escrever um programa em Python que lê o público total de um jogo de futebol e
fornecer a renda do jogo, sabendo-se que havia 4 tipos de ingressos assim distribuídos:
popular 10% a R$10,00, geral 50% a R$50,00, arquibancada 30% a R$100,00 e cadeiras
10% a R$ 200,00."""

publicoTotal = int(input("Digite o publico total: "))

quantidadePopular = publicoTotal * 0.1
quantidadeGeral = publicoTotal * 0.5
quantidadeArquibancada = publicoTotal * 0.3
quantidadeCadeiras = publicoTotal * 0.1

lucroPopular = quantidadePopular * 10.00
lucroGeral = quantidadePopular * 50.00
lucroArquibancada = quantidadePopular * 100.00
lucroCadeiras = quantidadePopular * 200.00

rendaTotal = lucroPopular+lucroArquibancada+lucroCadeiras+lucroGeral

print(f"A renda total arrecada foi de R${rendaTotal}.")