"""18. Uma organização resolveu dar um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver o programa que calculará os reajustes. Faça um
programa Python que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
a. o salário antes do reajuste;
b. o percentual de aumento aplicado;
c. o valor do aumento;
d. o novo salário, após o aumento."""

salario = float(input("Digite seu salário: "))
percentualAumento = 0
valorAumento = 0
novoSalario = 0

if salario <= 280:
    percentualAumento = 0.2
    valorAumento = salario*0.2
    novoSalario = salario+valorAumento
elif 280 < salario <= 700:
    percentualAumento = 0.15
    valorAumento = salario*0.15
    novoSalario = salario+valorAumento
elif 700 < salario <= 1500:
    percentualAumento = 0.1
    valorAumento = salario*0.1
    novoSalario = salario+valorAumento
else:
    percentualAumento = 0.05
    valorAumento = salario*percentualAumento
    novoSalario = salario+valorAumento

print(f"Salário antes: R${salario}\n"
    f"Percentual de aumento: {percentualAumento*100}%\n"
    f"Valor de aumento: R${valorAumento}\n"
    f"Novo salário: R${novoSalario}")
