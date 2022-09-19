"""11. Faça um programa Python que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em MBps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos)."""

tamanhoArquivo = int(input("Digite o tamanho do arquivo a ser baixado em MB: "))

velocidade = int(input("Digite a velocidade da internet em MBps: "))

tempoDownload = tamanhoArquivo/velocidade
# A equação do calculo de velocidade é tamanho do arquivo dividido por velocidade sobre 8,
# contudo esse cálculo usa a velocidade em bits, como a unidade deve ser bytes seria multiplicar e em seguida dividir por 8, logo só uma divisão.

tempoMinutos = int(tempoDownload // 60)
tempoSegundos = int(tempoDownload % 60)

print(f"O tempo de de download será de {tempoMinutos}min e {tempoSegundos}seg.")

