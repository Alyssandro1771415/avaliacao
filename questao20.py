"""20. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
tabela abaixo:  Média de Aproveitamento Conceito
 Entre 9.0 e 10.0 A
 Entre 7.5 e 9.0 B
 Entre 6.0 e 7.5 C
 Entre 4.0 e 6.0 D
 Entre 4.0 e zero E
O programa Python deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
conceito for D ou E."""

notaA = float(input("Primeira nota: "))
notaB = float(input("Segunda nota: "))

media = (notaA+notaB)/2

if 10 == media >= 9:
    conceito = "A"
    situacao = "Aprovado"
elif 9 > media >= 7.5:
    conceito = "B"
    situacao = "Aprovado"
elif 7.5 > media >= 6:
    conceito = "C"
    situacao = "Aprovado"
elif 4 > media >= 6:
    conceito = "D"
    situacao = "Reprovado"
else:
    conceito = "E"
    situacao = "Repreovado"