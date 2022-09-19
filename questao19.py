"""19. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas
não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao
Salário Bruto menos os descontos. O programa Python deverá pedir ao usuário o valor
da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações a seguir. No exemplo o valor da hora é 5 e a
quantidade de hora é 220. """

valorHora = float(input("Salário hora: "))
numeroHoras = int(input("Quantidade horas: "))

salarioBruto = valorHora*numeroHoras

if salarioBruto <= 900:
    IR = 00.00
    INSS = salarioBruto*0.03
    FGTS = salarioBruto*0.11
    totalDesconto = IR+INSS
    salarioLiquido = salarioBruto - totalDesconto
elif 900 < salarioBruto <= 1500:
    IR = salarioBruto * 0.05
    INSS = salarioBruto*0.03
    FGTS = salarioBruto*0.11
    totalDesconto = IR+INSS
    salarioLiquido = salarioBruto - totalDesconto
elif 1500 < salarioBruto <=2500:
    IR = salarioBruto*0.1
    INSS = salarioBruto*0.03
    FGTS = salarioBruto*0.11
    totalDesconto = IR+INSS
    salarioLiquido = salarioBruto - totalDesconto
else:
    IR = salarioBruto*0.2
    INSS = salarioBruto*0.03
    FGTS = salarioBruto*0.11
    totalDesconto = IR+INSS
    salarioLiquido = salarioBruto - totalDesconto

print(f"Salario bruto: R${salarioBruto}\n"
      f"IR: R${IR}\n"
      f"INSS: R${INSS}\n"
      f"FGTS: R${FGTS}\n"
      f"Total descontado: R${totalDesconto}\n"
      f"Salario líquido: R${salarioLiquido}\n")