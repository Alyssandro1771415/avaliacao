"""26. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
programa Python que calcule seu peso ideal, utilizando as seguintes fórmulas: para
homens: (72.7*h) – 58 e para mulheres: (62.1*h) - 44.7 (h = altura)"""

altura = float(input("Altura: "))
sexo = str(input("Sexo(M/F): ")).upper()

if sexo == "M":
    pesoIdeal = (72.7*altura) - 58
    print(f"Seu peso ideal é {pesoIdeal:.2f}Kg")
elif sexo == "F":
    pesoIdeal = (62.1*altura) - 44.7
    print(f"Seu peso ideal é {pesoIdeal:.2f}Kg")
else:
    print("Dados inválidos, reinicie o programa.")